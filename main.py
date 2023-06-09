import pyttsx3, pyaudio, vosk, requests
import json, os

tts = pyttsx3.init()

voices = tts.getProperty('voices')
tts.setProperty('voices', 'en')

for voice in voices:
    if voice.name == 'Microsoft David Desktop - English (United States)':
        tts.setProperty('voices', voice.id)

model = vosk.Model('model_small')
record = vosk.KaldiRecognizer(model, 16000)
aud = pyaudio.PyAudio()
stream = aud.open(format=pyaudio.paInt16,
                  channels=1,
                  rate=16000,
                  input=True,
                  frames_per_buffer=8000)
stream.start_stream()


def listening():
    while True:
        data = stream.read(4000, exception_on_overflow=False)
        if record.AcceptWaveform(data) and len(data) > 0:
            answer = json.loads(record.Result())
            if answer['text']:
                yield answer['text']


def speaking(say):
    tts.say(say)
    tts.runAndWait()


speaking('Starting')
print("Let's go...")

main_data = []
commands = {'занятие', 'тип', 'участники', 'стоимость', 'закрыть'}
for text in listening():
    print(text)
    if text == 'занятие':
        main_data = []
        res = requests.get("https://www.boredapi.com/api/activity")
        data = res.json()
        main_data = data
        print(main_data['activity'])
        speaking(str(main_data['activity']))

    if text == 'тип':
        if main_data != []:
            print(main_data['type'])
            speaking(str(main_data['type']))
        else:
            speaking('I do not know what action you are talking about')

    if text == 'участники':
        if main_data != []:
            print(main_data['participants'])
            speaking(str(main_data['participants']))
        else:
            speaking('I do not know what action you are talking about')

    if text == 'стоимость':
        if main_data != []:
            print(main_data['price'], 'dollars')
            speaking(str(main_data['price'])+'dollars')
        else:
            speaking('I do not know what action you are talking about')

    if text == 'закрыть':
        quit()

    if text not in commands:
        speaking('I have not learnt this word yet:(')

