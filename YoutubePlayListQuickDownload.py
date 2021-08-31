from pytube import Playlist
import os

p = Playlist(url=input('pls enter youtube playlist link：'))


if not os.path.exists(f'./{p.title}'):
    os.mkdir(f'./{p.title}')
    os.chdir(f'./{p.title}')
    print('floder created！')
else:
    print('floder created！')
    os.chdir(f'./{p.title}')


for z in p.videos:
    filename = z.streams.filter(only_audio=True).first().default_filename
    if os.path.isfile(f'./{filename}'):
        print('file already exist！')
        continue
    else:
        z.streams.filter(only_audio=True).first().download()
        print(f'{z.streams.filter(only_audio=True).first().default_filename}\ndownload success！')
