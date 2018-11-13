#!/usr/bin/env python3
import speech_recognition as sr
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor
import time
import atexit

mh = Adafruit_MotorHAT(addr=0x60)
MotorPort3 = mh.getMotor(1)
MotorPort4 = mh.getMotor(2)


def MotorenAbschalten():
    mh.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(2).run(Adafruit_MotorHAT.RELEASE)

def geradeFahren():
    MotorPort3.run(Adafruit_MotorHAT.BACKWARD)
    MotorPort3.setSpeed(100)

def rueckwaertsFahren():
    MotorPort3.run(Adafruit_MotorHAT.FORWARD)
    MotorPort3.setSpeed(100)

def rechtsFahren():
    MotorPort4.run(Adafruit_MotorHAT.BACKWARD)
    MotorPort4.setSpeed(250)
    MotorPort3.run(Adafruit_MotorHAT.BACKWARD)
    MotorPort3.setSpeed(75)

def linksFahren():
    MotorPort4.run(Adafruit_MotorHAT.BACKWARD)
    MotorPort4.setSpeed(250)
    MotorPort3.run(Adafruit_MotorHAT.BACKWARD)
    MotorPort3.setSpeed(75)


while True:
    r = sr.Recognizer()
    with sr.Microphone(device_index=2) as source:
        print("Höre zu...")
        audio = r.listen(source)

    try:
        vartext = ''
        vartext = r.recognize_google(audio, language="de_DE")
        if (vartext == 'start') or (vartext == 'starten') or (vartext == 'losfahren'):
            geradeFahren()
            print ('Auto fährt gerade los')
        elif (vartext == 'rechts abbiegen') or (vartext == 'rechts'):
            rechtsFahren()
            print('Auto biegt rechts ab')
        elif (vartext == 'links abbiegen') or (vartext == 'links'):
            linksFahren()
            print('Auto biegt links ab')
        elif (vartext == 'stop') or (vartext == 'anhalten'):
            MotorenAbschalten()
            print('Auto haltet an')
        elif (vartext == 'nach hinten') or (vartext == 'rückwärts'):
            rueckwaertsFahren()
            print('Nach hinten Fahren')
        else:
            print(vartext)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

atexit.register(MotorenAbschalten)
