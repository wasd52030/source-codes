from pytube import Playlist
import os
import subprocess

p = Playlist(url=input("pls enter youtube playlist link："))


if not os.path.exists(f"./{p.title}"):
    os.mkdir(f"./{p.title}")
    os.chdir(f"./{p.title}")
    print("floder created！")
else:
    print("floder created！")
    os.chdir(f"./{p.title}")

for index, item in enumerate(p.videos):
    item.streams.filter(only_audio=True).first().download()
    mp4name = item.streams.filter(only_audio=True).first().default_filename
    mp3name = f"{item.streams.filter(only_audio=True).first().default_filename[:-4]}.mp3"

    #調ffmpeg來把下載下來的mp4轉成mp3
    subprocess.run([
        os.path.join(os.path.abspath(os.path.join(os.getcwd(), os.path.pardir)), "ffmpeg.exe"),
        "-i",
        os.path.join(os.getcwd(), mp4name),
        os.path.join(os.getcwd(), mp3name)
    ], capture_output=True)

    os.remove(os.path.join(os.getcwd(), mp4name)) #刪掉原本的mp4
    print(f"{mp3name}\ndownload success！\n{index+1}/{len(p.videos)}\n")