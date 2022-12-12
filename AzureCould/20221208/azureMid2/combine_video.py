import ffmpeg
from utils import Logger

@Logger
def combine_video(filepath, filename,substitleFilePath):
    video = (
        ffmpeg.input(filepath)
        .filter('subtitles', substitleFilePath)
    )

    audio = (
        ffmpeg.input(f'./statics/{filename}.wav')
    )

    (
        ffmpeg.concat(video, audio, v=1, a=1)
        .output(f'./result/{filename}_subtitled.mp4')
        .overwrite_output()
        .run()
    )
