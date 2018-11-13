#!/usr/bin/env python3
import redis
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor

r = redis.StrictRedis(host='localhost', port=6379, db=0)
mh = Adafruit_MotorHAT(addr=0x60)
MotorPort1 = mh.getMotor(1)
MotorPort2 = mh.getMotor(2)
while True:
    # Sensor Daten aus Redis DB auslesen
    varvorne = r.get('vorne')
    varhinten = r.get('hinten')

    if (varvorne <= '4') or (varhinten <= '4'):
        MotorPort1.setSpeed(0)