import asyncio
import json
import re
from dataclasses import dataclass
from typing import Union, Sequence
import httpx
import json5

from bilix.dm import parse_view
from bilix.utils import req_retry, legal_title

_dft_headers = {'user-agent': 'PostmanRuntime/7.29.0', 'referer': 'https://www.bilibili.com'}
_dft_client = httpx.AsyncClient(headers=_dft_headers, http2=True)


async def get_cate_meta(client: httpx.AsyncClient = _dft_client) -> dict:
    """
    获取b站分区元数据

    :param client:
    :return:
    """
    cate_info = {}
    res = await req_retry(client, 'https://s1.hdslb.com/bfs/static/laputa-channel/client/assets/index.c0ea30e6.js')
    cate_data = re.search('Za=([^;]*);', res.text).groups()[0]
    cate_data = json5.loads(cate_data)['channelList']
    for i in cate_data:
        if 'sub' in i:
            for j in i['sub']:
                cate_info[j['name']] = j
            cate_info[i['name']] = i
    return cate_info


async def get_list_info(url_or_sid: str, client: httpx.AsyncClient = _dft_client):
    """
    获取视频列表信息

    :param url_or_sid:
    :param client:
    :return:
    """
    if url_or_sid.startswith('http'):
        sid = re.search(r'sid=(\d+)', url_or_sid).groups()[0]
    else:
        sid = url_or_sid
    res = await req_retry(client, f'https://api.bilibili.com/x/series/series?series_id={sid}')  # meta api
    meta = json.loads(res.text)
    mid = meta['data']['meta']['mid']
    params = {'mid': mid, 'series_id': sid, 'ps': meta['data']['meta']['total']}
    list_res, up_res = await asyncio.gather(
        req_retry(client, 'https://api.bilibili.com/x/series/archives', params=params),
        req_retry(client, f'https://api.bilibili.com/x/space/acc/info?mid={mid}'))
    list_info, up_info = json.loads(list_res.text), json.loads(up_res.text)
    list_name, up_name = meta['data']['meta']['name'], up_info['data']['name']
    bvids = [i['bvid'] for i in list_info['data']['archives']]
    return list_name, up_name, bvids


async def get_collect_info(url_or_sid, client: httpx.AsyncClient = _dft_client):
    """
    获取合集信息

    :param url_or_sid:
    :param client:
    :return:
    """
    sid = re.search(r'sid=(\d+)', url_or_sid).groups()[0] if url_or_sid.startswith('http') else url_or_sid
    params = {'season_id': sid}
    res = await req_retry(client, 'https://api.bilibili.com/x/space/fav/season/list', params=params)
    data = json.loads(res.text)
    medias = data['data']['medias']
    info = data['data']['info']
    col_name, up_name = info['title'], medias[0]['upper']['name']
    bvids = [i['bvid'] for i in data['data']['medias']]
    return col_name, up_name, bvids


async def get_favour_page_info(fid, pn=1, ps=20, keyword='', client: httpx.AsyncClient = _dft_client):
    """
    获取收藏夹信息（分页）

    :param fid:
    :param pn:
    :param ps:
    :param keyword:
    :param client:
    :return:
    """
    params = {'media_id': fid, 'pn': pn, 'ps': ps, 'keyword': keyword, 'order': 'mtime'}
    res = await req_retry(client, 'https://api.bilibili.com/x/v3/fav/resource/list', params=params)
    data = json.loads(res.text)['data']
    fav_name, up_name = data['info']['title'], data['info']['upper']['name']
    bvids = [i['bvid'] for i in data['medias'] if i['title'] != '已失效视频']
    total_size = data['info']['media_count']
    return fav_name, up_name, total_size, bvids


async def get_cate_page_info(cate_id, time_from, time_to, pn=1, ps=30, order='click', keyword='',
                             client: httpx.AsyncClient = _dft_client):
    """
    获取分区视频信息（分页）

    :param cate_id:
    :param pn:
    :param ps:
    :param order:
    :param keyword:
    :param time_from:
    :param time_to:
    :param client:
    :return:
    """
    params = {'search_type': 'video', 'view_type': 'hot_rank', 'cate_id': cate_id, 'pagesize': ps,
              'keyword': keyword, 'page': pn, 'order': order, 'time_from': time_from, 'time_to': time_to}
    res = await req_retry(client, 'https://s.search.bilibili.com/cate/search', params=params)
    info = json.loads(res.text)
    bvids = [i['bvid'] for i in info['result']]
    return bvids


async def get_up_info(mid, pn=1, ps=30, order='pubdate', keyword='', client=_dft_client):
    """
    获取up主信息

    :param mid:
    :param pn:
    :param ps:
    :param order:
    :param keyword:
    :param client:
    :return:
    """
    params = {'mid': mid, 'order': order, 'ps': ps, 'pn': pn, 'keyword': keyword}
    res = await req_retry(client, 'https://api.bilibili.com/x/space/arc/search', params=params)
    info = json.loads(res.text)
    up_name = info['data']['list']['vlist'][0]['author']
    total_size = info['data']['page']['count']
    bv_ids = [i['bvid'] for i in info['data']['list']['vlist']]
    return up_name, total_size, bv_ids


@dataclass
class VideoInfo:
    title: str
    h1_title: str
    aid: Union[str, int]
    cid: Union[str, int]
    p: int
    pages: Sequence[Sequence[str]]
    img_url: str
    bvid: str = None
    dash: dict = None


async def get_video_info(url, client=_dft_client) -> VideoInfo:
    """
    获取视频信息

    :param url:
    :param client:
    :return:
    """
    res = await req_retry(client, url, follow_redirects=True)
    init_info = re.search(r'<script>window.__INITIAL_STATE__=({.*});\(', res.text).groups()[0]  # this line may raise
    init_info = json.loads(init_info)
    if len(init_info.get('error', {})) > 0:
        raise AttributeError("视频已失效")  # 啊叻？视频不见了？在分区下载的时候可能产生
    # extract meta
    pages = []
    h1_title = legal_title(re.search('<h1[^>]*title="([^"]*)"', res.text).groups()[0])
    if 'videoData' in init_info:  # bv视频
        bvid = init_info['bvid']
        aid = init_info['aid']
        (p, cid), = init_info['cidMap'][bvid]['cids'].items()
        p = int(p) - 1
        title = legal_title(init_info['videoData']['title'])
        base_url = url.split('?')[0]
        for idx, i in enumerate(init_info['videoData']['pages']):
            p_url = f"{base_url}?p={idx + 1}"
            add_name = f"P{idx + 1}-{i['part']}" if len(init_info['videoData']['pages']) > 1 else ''
            pages.append([add_name, p_url])
    elif 'initEpList' in init_info:  # 动漫，电视剧，电影
        bvid = None
        aid = init_info['epInfo']['aid']
        cid = init_info['epInfo']['cid']
        p = init_info['epInfo']['i']
        title = legal_title(re.search('property="og:title" content="([^"]*)"', res.text).groups()[0])
        for idx, i in enumerate(init_info['initEpList']):
            p_url = i['link']
            add_name = i['title']
            pages.append([add_name, p_url])
    else:
        raise AttributeError("未知类型")
    # extract dash
    try:
        play_info = re.search('<script>window.__playinfo__=({.*})</script><script>', res.text).groups()[0]
        play_info = json.loads(play_info)
        dash = play_info['data']['dash']
    except (KeyError, AttributeError):  # KeyError-电影，AttributeError-动画
        # todo https://www.bilibili.com/video/BV1Jx411r776?p=3 未处理，没有dash下载方式的视频
        dash = None
    # extract img url
    img_url = re.search('property="og:image" content="([^"]*)"', res.text).groups()[0]
    # construct data
    video_info = VideoInfo(title=title, h1_title=h1_title, aid=aid, cid=cid,
                           p=p, pages=pages, img_url=img_url, bvid=bvid, dash=dash)
    return video_info


async def get_subtitle_info(bvid, cid, client=_dft_client):
    params = {'bvid': bvid, 'cid': cid}
    res = await req_retry(client, 'https://api.bilibili.com/x/player/v2', params=params)
    info = json.loads(res.text)
    if info['code'] == -400:
        raise AttributeError(f'未找到字幕信息')
    return [[f'http:{i["subtitle_url"]}', i['lan_doc']] for i in info['data']['subtitle']['subtitles']]


async def get_dm_info(aid, cid, client=_dft_client):
    params = {'oid': cid, 'pid': aid, 'type': 1}
    res = await req_retry(client, f'https://api.bilibili.com/x/v2/dm/web/view', params=params)
    view = parse_view(res.content)
    total = int(view['dmSge']['total'])
    return [f'https://api.bilibili.com/x/v2/dm/web/seg.so?oid={cid}&type=1&segment_index={i + 1}' for i in range(total)]


if __name__ == '__main__':
    import rich

    # result = asyncio.run(get_cate_meta())
    # rich.print(result)
    result = asyncio.run(get_favour_page_info(
        "69072721"
    ))
    rich.print(result)
