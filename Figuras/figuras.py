# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 19:51:57 2021

@author: Alberto Alvarado

Algoritmo de los cuadrados
"""

import numpy as np
from time import time
def primo(n):
    band = 1
    for i in range(1, int(np.sqrt(n))):
        if  n % i== 0:
            band = 0
    return band


def clasificar(area):
    
    if(area == 1):
        return "Cuadrado"
    
    lado = int(np.sqrt(area))
    
    if(lado * lado == area):
        if(primo(lado) == 1 and 2 % lado != 0):
            return "Es un cuadrado"
        else:
            return "Podría ser ambos"
    else:
            return "Es un rectángulo"
    

area = int(input("Introduce el área:  "))
start_time = time()
if(area < 1 or area > 1000000):
    print("\nArea no válida")

else:
    
    print("Su figura "+clasificar(area))

elapsed_time = time() - start_time
print("Tiempo tardado: %.10f seg." % elapsed_time)