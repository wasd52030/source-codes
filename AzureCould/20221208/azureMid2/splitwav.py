from utils import Logger
import ffmpeg


@Logger
def splitwav(orginFilePath, targetFilePath):
    (
        ffmpeg.input(orginFilePath)
        .output(targetFilePath)
        .overwrite_output()
        .run()
    )
