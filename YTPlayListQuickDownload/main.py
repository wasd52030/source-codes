# 請把ffmpeg.exe放進跟程式檔同一目錄下

from pytube import Playlist
import os
import subprocess
from concurrent.futures import ThreadPoolExecutor


def download(item):
    try:
        item.streams.filter(only_audio=True).first().download()
        mp4name = item.streams.filter(only_audio=True).first().default_filename
        mp3name = f"{mp4name[:-4]}.mp3"

        # 調ffmpeg來把下載下來的mp4轉成mp3
        subprocess.run([
            os.path.join(
                os.path.abspath(os.path.join(os.getcwd(), os.path.pardir)),
                "ffmpeg.exe"
            ),
            "-i",
            os.path.join(os.getcwd(), mp4name),
            os.path.join(os.getcwd(), mp3name)
        ], capture_output=True)

        os.remove(os.path.join(os.getcwd(), mp4name))  # 刪掉原本的mp4
        print(f"{mp3name}\ndownload success！\n")
    except:
        print("ERROR！")



if __name__ == "__main__":
    p = Playlist(url=input("pls enter youtube playlist link："))

    if not os.path.exists(f"./{p.title}"):
        os.mkdir(f"./{p.title}")
        os.chdir(f"./{p.title}")
        print("floder created！")
    else:
        print("floder created！")
        os.chdir(f"./{p.title}")

    #max_workers請斟酌設定
    with ThreadPoolExecutor(max_workers=8) as executer:
        executer.map(download, p.videos)
