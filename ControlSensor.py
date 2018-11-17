#!/usr/bin/env python3
import redis
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor

r = redis.StrictRedis(host='localhost', port=6379, db=0)

while True:
    # Sensor Daten aus Redis DB auslesen
    varvorne = r.get('vorne').decode('utf8').strip()
    varhinten = r.get('hinten').decode('utf8').strip()

    if (varvorne <= '10') or (varhinten <= '10'):
        mh = Adafruit_MotorHAT(addr=0x60)
        MotorPort1 = mh.getMotor(1)
        MotorPort2 = mh.getMotor(2)
        MotorPort1.setSpeed(0)