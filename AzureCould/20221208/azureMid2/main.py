import fileHelper
from captioning import makeSubtitles
from translate import translate
from splitwav import splitwav
from combine_video import combine_video


if __name__ == '__main__':

    filepath = r'./statics/Flutter Google Map With Live Location Tracking.mp4'
    filename = filepath.split('/')[-1][:-4]

    fileHelper.manageFolder('./substitles')
    fileHelper.manageFolder('./result')

    # https://learn.microsoft.com/zh-tw/azure/cognitive-services/speech-service/language-support?tabs=stt-tts
    origin, target = 'en-US', 'zh-Hant'

    audiofilepath = f'./statics/{filename}.wav'
    splitwav(
        orginFilePath=filepath,
        targetFilePath=audiofilepath
    )

    substitleFilePath = f'./substitles/{filename}.srt'
    makeSubtitles(
        filePath=audiofilepath,
        outputPath=substitleFilePath,
        lang=origin
    )
    with open(substitleFilePath, 'r', encoding='utf-8') as f:
        translate(
            ''.join(f.readlines()),
            origin, target,
            substitleFilePath
        )

    combine_video(
        filepath=filepath,
        filename=filename,
        substitleFilePath=substitleFilePath
    )
