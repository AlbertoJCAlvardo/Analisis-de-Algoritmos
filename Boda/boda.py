# -*- coding: utf-8 -*-
"""
Created on Sun May 23 20:04:49 2021

@author: ALVARADO

Problema de la boda
"""

def notin(x,l):
    for i in l:
        for j in i:
            if j == x:
                return False
    return True

def recorrerMatriz(m):
    
    mesas = []
    k = 0
    
    for i in range(0, len(m)):
        if(notin(i, mesas)  == True and i != 0):
            mesas.append([i])
            k+=1
            for j in range(0, len(m)):
                if m[i][j] == 1:
                    mesas[k-1].append(j)
                
        if(i == 0):
            mesas.append([i])
            k+=1
            for j in range(0, len(m)):
                if m[i][j] == 1:
                    mesas[k-1].append(j)
                
    return mesas

def recorrerLista(l):
    mesas = []
    k = 0
    
    for i in range(0, len(l)):
        if notin(i, mesas):
            aux = l[i]
            aux.append(i)
            mesas.append(aux)
        
        
    return mesas
            
            


invitados = {0:'Tia Juana',
             1:'Mamá',
             2:'Prima Moderna',
             3:'El Jefe',
             4:'La charito',
             5:'El Cuñado',
             6:'Mi Ex',
             7:'Ella '
            }
            
    

matriz_adyacencia = [
                        [0,1,1,0,0,0,0,0,0],
                        [1,0,1,0,0,0,0,0,0],
                        [1,1,0,0,0,0,0,0,0],
                        [0,0,0,0,1,1,0,0,0],
                        [0,0,0,1,0,1,0,0,0],
                        [0,0,0,1,1,0,0,0,0],
                        [0,0,0,0,0,0,0,1,0],
                        [0,0,0,0,0,0,1,0,0],
                    ]

lista_adyacencia = [
                    [1,2],
                    [0,2],
                    [0,1],
                    [4,5],
                    [3,5],
                    [3,4],
                    [7],
                    [6],
                    
                    ]

mesas1 = recorrerMatriz(matriz_adyacencia)

print("\n\nImplementación con matriz de adyacencia: \n\n")
k = 0
for i in mesas1:
    k+=1
    print('\nMesa '+str(k)+": ")
    for j in i:
        print("\t"+str(invitados[j]))
        
print("Implementación con lista de adyacencia: \n\n")


mesas2 = recorrerLista(lista_adyacencia)

k = 0
for i in mesas2:
    k+=1
    print('\nMesa '+str(k)+": ")
    for j in i:
        print("\t"+str(invitados[j]))
