# 請把ffmpeg.exe放進跟程式檔同一目錄下

from glob import glob
from urllib.parse import parse_qs, urlparse
import traceback
import html
import asyncio
import requests
import os
import subprocess
from concurrent.futures import ThreadPoolExecutor
from Downloader import Downloader
from funcTimer import FuncTimer


async def download(id, num):
    d = Downloader(videos_dir=os.curdir, video_concurrency=5)
    await d.get_favour(fid=id, quality=100, num=num, keyword='', series=False)
    await d.aclose()


def ToMp3(video):
    global length, cnt

    try:
        subprocess.run([
            os.path.join(
                os.path.abspath(os.path.join(os.getcwd(), os.path.pardir)),
                "ffmpeg.exe"
            ),
            "-i",
            os.path.join(os.getcwd(), video),
            os.path.join(
                os.getcwd(),
                str(html.unescape(video)).replace("mp4", "mp3")
            )
        ], capture_output=True)

        os.remove(os.path.join(os.getcwd(), video))  # 刪掉原本的mp4

        cnt += 1
        print(f"{html.unescape(video)} 轉換完成，目前進度: {cnt}/{length}")
    except:
        print(traceback.format_exc())


@FuncTimer
def main():
    global cnt, length

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
    print("mp4下載完成，將轉成mp3")

    mp4s = os.listdir('./')
    cnt, length = 0, len(mp4s)
    with ThreadPoolExecutor(max_workers=20) as executer:
        executer.map(ToMp3, mp4s)
    print("全部mp3轉換完成")


if __name__ == "__main__":
    cnt, length = 0, 0
    main()
