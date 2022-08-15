# 請把ffmpeg.exe放進跟程式檔同一目錄下

from urllib.parse import parse_qs, urlparse
import asyncio
import requests
import os
from bilix.download import Downloader
from funcTimer import FuncTimer


async def download(id, num):
    d = Downloader(videos_dir=os.curdir, video_concurrency=5)
    await d.get_favour(fid=id, quality=100, num=num, keyword='', series=False, only_audio=True, hierarchy=False)
    await d.aclose()


@FuncTimer
def main():
    global cnt, length

    """
        urlprase函數裡面填要下載的收藏夾網址
    """
    url = urlparse(
        'https://space.bilibili.com/15007690/favlist?fid=171091690&ftype=create'
    )
    parameters = parse_qs(url.query)

    FavourInfo = requests.get(
        f"https://api.bilibili.com/x/v3/fav/resource/list?media_id={parameters['fid'][0]}&ps=1"
    ).json()['data']['info']

    if not os.path.exists(f"./Bilibili-{FavourInfo['title']}"):
        os.mkdir(f"./Bilibili-{FavourInfo['title']}")
        os.chdir(f"./Bilibili-{FavourInfo['title']}")
        print("floder created！")
    else:
        print("floder created！")
        os.chdir(f"./Bilibili-{FavourInfo['title']}")

    asyncio.run(download(FavourInfo['id'], FavourInfo['media_count']))
    print("下載完成")


if __name__ == "__main__":
    cnt, length = 0, 0
    main()
