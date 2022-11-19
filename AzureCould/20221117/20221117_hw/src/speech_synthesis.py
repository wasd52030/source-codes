import azure.cognitiveservices.speech as speechsdk

speech_config = speechsdk.SpeechConfig(
    subscription='f9422c78597d4136910992d17656abf6',
    region='eastus',
)
audio_config = speechsdk.audio.AudioOutputConfig(filename="results/synth_result.wav")

# reference -> https://learn.microsoft.com/en-us/azure/cognitive-services/speech-service/language-support?tabs=stt-tts
speech_config.speech_synthesis_voice_name = 'zh-TW-HsiaoChenNeural'

speech_synthesizer = speechsdk.SpeechSynthesizer(
    speech_config=speech_config,
    audio_config=audio_config
)

# txt is copy form https://zh.wikipedia.org/zh-tw/Python
input_file="static/text_input.txt"
print(f"synthesize from file {input_file}...")
with open(input_file, encoding="UTF-8") as f:
    text = "".join(f.readlines())

speech_synthesis_result = speech_synthesizer.speak_text_async(text).get()

if speech_synthesis_result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
    print("Speech synthesized for text [{}]".format(text))
elif speech_synthesis_result.reason == speechsdk.ResultReason.Canceled:
    cancellation_details = speech_synthesis_result.cancellation_details
    print("Speech synthesis canceled: {}".format(cancellation_details.reason))
    if cancellation_details.reason == speechsdk.CancellationReason.Error:
        if cancellation_details.error_details:
            print("Error details: {}".format(cancellation_details.error_details))
            print("Did you set the speech resource key and region values?")
