# 請把ffmpeg.exe放進跟程式檔同一目錄下

from pytube import Playlist, YouTube
import os
import subprocess
from concurrent.futures import ThreadPoolExecutor
import traceback
from funcTimer import FuncTimer


def download(item: YouTube) -> None:
    global cnt, length

    try:
        item.streams.filter(only_audio=True).first().download()
        video = item.streams.filter(only_audio=True).first().default_filename
        print(f'{video}下載完成，即將轉換成Mp3')
        #mp3name = f"{video[:-4]}.mp3"

        # 調ffmpeg來把下載下來的mp4轉成mp3
        subprocess.run([
            os.path.join(
                os.path.abspath(os.path.join(os.getcwd(), os.path.pardir)),
                "ffmpeg.exe"
            ),
            "-i",
            os.path.join(os.getcwd(), video),
            os.path.join(os.getcwd(), str(video).replace("mp4", "mp3"))
        ], capture_output=True)

        os.remove(os.path.join(os.getcwd(), video))  # 刪掉原本的mp4
        print(f"{str(video).replace('mp4','mp3')}\n轉換完成！")

        cnt += 1
        print(f"{cnt}/{length}\n")
    except:
        print(traceback.format_exc())


@FuncTimer
def main() -> None:
    global length

    # https://www.youtube.com/playlist?list=PLdx_s59BrvfXJXyoU5BHpUkZGmZL0g3Ip
    p = Playlist(url=input("pls enter youtube playlist link："))
    length = p.length

    if not os.path.exists(f"./YT-{p.title}"):
        os.mkdir(f"./YT-{p.title}")
        os.chdir(f"./YT-{p.title}")
        print("floder created！")
    else:
        print("floder created！")
        os.chdir(f"./YT-{p.title}")

    # max_workers請斟酌設定
    with ThreadPoolExecutor(max_workers=10) as executer:
        executer.map(download, p.videos)


if __name__ == "__main__":
    cnt, length = 0, 0
    main()
