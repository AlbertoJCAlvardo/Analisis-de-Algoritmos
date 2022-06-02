# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 17:47:57 2021

@author: Alberto Alvarado Sandoval

Títilo: Examen Análisis de Algoritmos Primer corte
"""

    

def CP(n, C, N):
    if(n == 0):
        return 0
    if n == 1:
        return C;
    
    return CP(n-1, C, N)- C/N;


def I(n, C, N):
    return 0.3 * CP(n, C, N);




def  M(n, C, N):
    if(n == 0):
        return 1
    elif(n == 1):
        return 0.3*C + C/N;
    elif CP(n, C, N) < 0:
        return 0;
    else:
        return I(n, C, N) + CP(n,C, N)/N;


def hipoteca(meses, Capital):
    monto_total = 0
    for i in range(1, meses + 1):
        x = M(i, Capital, n)
        print("En el mes: "+str(i)+" Debes pagar $"+str(x))
        monto_total += x
    return monto_total



C = 20000
n = 12
m = hipoteca(n, C)
print(m)