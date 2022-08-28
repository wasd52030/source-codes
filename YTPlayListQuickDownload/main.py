# 請確認已將ffmpeg下載到電腦中並設定環境變數！

import os
import subprocess
from concurrent.futures import ThreadPoolExecutor, as_completed
import traceback

from pytube import Playlist, YouTube
from tqdm import tqdm


def download(item: YouTube) -> None:

    try:
        item.streams.filter(only_audio=True).first().download()
        video = item.streams.filter(only_audio=True).first().default_filename

        # 調ffmpeg來把下載下來的mp4轉成mp3
        subprocess.run([
            "ffmpeg.exe",
            "-i",
            os.path.join(os.getcwd(), video),
            os.path.join(os.getcwd(), str(video).replace("mp4", "mp3"))
        ], capture_output=True)

        os.remove(os.path.join(os.getcwd(), video))  # 刪掉原本的mp4
    except:
        print(traceback.format_exc())


def main() -> None:

    PlayListUrl = 'https://www.youtube.com/playlist?list=PLdx_s59BrvfXJXyoU5BHpUkZGmZL0g3Ip'
    p = Playlist(url=PlayListUrl)

    if not os.path.exists(f"./YT-{p.title}"):
        os.mkdir(f"./YT-{p.title}")
        os.chdir(f"./YT-{p.title}")
        print("floder created！")
    else:
        print("floder created！")
        os.chdir(f"./YT-{p.title}")

    progressBar = tqdm(total=p.length, desc='下載進度')  # 進度條
    with ThreadPoolExecutor(max_workers=20) as executer:
        futures = [executer.submit(download, video) for video in p.videos]
        for _ in as_completed(futures):
            progressBar.update(n=1)


if __name__ == "__main__":
    main()
