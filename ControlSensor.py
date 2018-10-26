#!/usr/bin/env python3
import redis
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor

r = redis.StrictRedis(host='localhost', port=6379, db=0)

while True:
    # Sensor Daten aus Redis DB auslesen
    varvorne = r.get('vorne')
    varhinten = r.get('hinten')
    # Definition Motor Objekt
    mh = Adafruit_MotorHAT(addr=0x60)
    MotorPort3 = mh.getMotor(3)
    MotorPort4 = mh.getMotor(4)
    if (varvorne <= '4') or (varhinten <= '4'):
        MotorPort4.setSpeed(0)

    else:
        MotorPort4.setSpeed(100)