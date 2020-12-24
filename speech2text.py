import speech_recognition as sr
import time
from telegrambot import fetchAudio,simplesend
from convert import toWav
st = time.time()

while True:
    flag = fetchAudio()
    if flag:
        print(1)
        toWav()
        print(2)
        r = sr.Recognizer()
        hd = sr.AudioFile('audio.wav')
        with hd as source:
            audio = r.record(source)
            print(type(audio))
            text = r.recognize_google(audio)
            print(text)
            simplesend(text)

print(time.time()-st)
