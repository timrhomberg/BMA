#!/usr/bin/env python3
import speech_recognition as sr
import time

r = sr.Recognizer()
with sr.Microphone(device_index=2) as source:
        print("Höre zu...")
        audio = r.listen(source)

BING_KEY = "da305e9fda73496fb180cb28756572e0"
try:
    vartext = r.recognize_bing(audio, key=BING_KEY, language="de-DE")
    vartext = vartext.lower()
    print(vartext)
    print("Microsoft Bing Voice Recognition thinks you said " + vartext)
except sr.UnknownValueError:
    print("Microsoft Bing Voice Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Microsoft Bing Voice Recognition service; {0}".format(e))