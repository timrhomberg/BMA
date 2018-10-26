#!/usr/bin/env python3
import serial
import redis

ser = serial.Serial('/dev/ttyUSB0',9600)
i = 0
r = redis.StrictRedis(host='localhost', port=6379, db=0)

while True:
        try:
                read_serial=ser.readline()
                serialoutput = read_serial.decode('utf8').strip()
                #print (serialoutput)
                i = i + 1
                #print (i)

                if i >= 3:
                        v1, v2 = serialoutput.split(', ')
                        print (v1)
                        print (v2)
                        r.set('vorne', v1)
                        r.set('hinten', v2)
        except:
                print  ('Daten konnten vom Sensor nicht übermittelt und transfomriert werden.')
                #raise