#!/usr/bin/env python3
import speech_recognition as sr
import sys
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor
import time
import atexit

def MotorenAbschalten():
    mh.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(4).run(Adafruit_MotorHAT.RELEASE)

def geradeFahren():
    MotorPort4.run(Adafruit_MotorHAT.FORWARD)
    MotorPort4.setSpeed(100)

def rueckwaertsFahren():
    MotorPort4.run(Adafruit_MotorHAT.BACKWARD)
    MotorPort4.setSpeed(100)

def rechtsFahren():
    MotorPort4.run(Adafruit_MotorHAT.FORWARD)
    MotorPort4.setSpeed(100)
    MotorPort3.run(Adafruit_MotorHAT.FORWARD)
    MotorPort3.setSpeed(50)

def linksFahren():
    MotorPort4.run(Adafruit_MotorHAT.FORWARD)
    MotorPort4.setSpeed(100)
    MotorPort3.run(Adafruit_MotorHAT.BACKWARD)
    MotorPort3.setSpeed(50)

atexit.register(MotorenAbschalten)

while True:
    mh = Adafruit_MotorHAT(addr=0x60)
    MotorPort3 = mh.getMotor(3)
    MotorPort4 = mh.getMotor(4)

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Höre zu...")
        audio = r.listen(source)
        varText = r.recognize_google(audio, language="de_DE")
        varText = varText.lower()
        print (varText)
        varText = {
            "start":geradeFahren(),
            "stop": MotorenAbschalten(),
            "rechts": rechtsFahren(),
            "links": linksFahren()
        }
    # Alle Motoren stoppen
    atexit.register(MotorenAbschalten)