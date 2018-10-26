#!/usr/bin/env python3
import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone(device_index=2) as source:
    print("Höre zu...")
    audio = r.listen(source)

try:
    print("Google Speech Recognition thinks you said " + r.recognize_google(audio))
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))
