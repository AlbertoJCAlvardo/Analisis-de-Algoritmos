
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  1 23:49:03 2021

@author: argen
"""

from serial import Serial
import time


try:
    arduino = Serial('COM4', 9600)
    
    while True: 
        dato = arduino.readline()
        print(dato)
    arduino.close()
except:
    print("A")