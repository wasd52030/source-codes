import azure.cognitiveservices.speech as speechsdk
import time


def recognize_from_file():
    results = []

    speech_config = speechsdk.SpeechConfig(
        subscription='f9422c78597d4136910992d17656abf6',
        region='eastus',
    )

    # reference -> https://learn.microsoft.com/en-us/azure/cognitive-services/speech-service/language-support?tabs=stt-tts
    speech_config.speech_recognition_language = "zh-TW"

    # wav file resource: https://www.youtube.com/shorts/F96h76Z8Seg
    recognize_file = "static/speech_input.wav"
    audio_config = speechsdk.audio.AudioConfig(filename=recognize_file)
    speech_recognizer = speechsdk.SpeechRecognizer(
        speech_config=speech_config,
        audio_config=audio_config
    )

    print(f"recognizing from file {recognize_file}...")


    done = False
    def stop_cb(enevt):
        print('CLOSING on {}'.format(enevt))
        speech_recognizer.stop_continuous_recognition()
        # reference -> https://ktinglee.github.io/LearningPython100days(6)_global_and_nonlocal
        nonlocal done
        done = True

    speech_recognizer.recognized.connect(
        lambda enevt: results.append(enevt.result.text))
    speech_recognizer.session_stopped.connect(stop_cb)
    speech_recognizer.canceled.connect(stop_cb)

    speech_recognizer.start_continuous_recognition()
    while not done:
        time.sleep(.5)
    else:
        with open("results/reco_result.txt", "w", encoding="UTF-8") as f:
            print(*results, file=f)


recognize_from_file()
