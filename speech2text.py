import speech_recognition as sr
import time
from telegrambot import fetchAudio,simplesend
from convert import toWav
st = time.time()

while True:
    flag,filename = fetchAudio()
    if flag:
        print(1)
        toWav(filename)
        print(2)
        r = sr.Recognizer()
        hd = sr.AudioFile("audio_files/"+filename.split(".")[0]+".wav")
        with hd as source:
            audio = r.record(source)
            print(type(audio))
            text = r.recognize_google(audio)
            print(text)
            simplesend(text)

print(time.time()-st)
