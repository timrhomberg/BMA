#!/usr/bin/env python3
import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone(device_index=2) as source:
    print("Höre zu...")
    audio = r.listen(source)

try:
    vartext = ''
    vartext = r.recognize_google(audio, language="de_DE")
    if (vartext == 'start') or (vartext == 'starten'):
        print ('Auto fährt gerade los')
    elif (vartext == 'rechts abbiegen') or (vartext == 'rechts'):
        print('Auto biegt rechts ab')
    else:
        print(vartext)
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))
