#!/usr/bin/env python3
import speech_recognition as sr

while True:
    r = sr.Recognizer()
    with sr.Microphone(device_index=2) as source:
        print("Höre zu...")
        audio = r.listen(source)

    try:
        vartext = ''
        vartext = r.recognize_google(audio, language="de_DE")
        if (vartext == 'start') or (vartext == 'starten') or (vartext == 'losfahren'):
            print ('Auto fährt gerade los')
        elif (vartext == 'rechts abbiegen') or (vartext == 'rechts'):
            print('Auto biegt rechts ab')
        elif (vartext == 'links abbiegen') or (vartext == 'links'):
            print('Auto biegt links ab')
        elif (vartext == 'stop') or (vartext == 'anhalten'):
            print('Auto haltet an')
        else:
            print(vartext)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))