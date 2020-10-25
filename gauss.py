# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 11:39:57 2020

@author: kevin
"""
import auxclass as aux

def isHomogeneous(l,m,n):#Vemos si es Homogenea
    t=aux.strlist(m)
    lt=aux.strlist(m)
    
    for i in range(0,m):
        t[i]=0
    for i in range(0,m):
        for j in range(0,n+1):
            if(j==n):
                lt[i]=l[i][j]
    if(lt==t):
        return True
    else:
        return False

def Diagonalize(l,m,n):
    k = 0
    #Copia de la matriz
    lt = aux.copy(l,m)
    while(k<m-1):#De Fila 1 a Fila n
        pivot = l[k][k]#pivote
        for i in range(k,m):#Fila
            cons = -lt[i][k]
            for j in range(0,n+1):#Columna
                if(i==k):
                    continue
                else:
                    l[i][j]=l[i][j]+((cons/pivot)*lt[k][j])
        k += 1#Cambiamos de Fila
    return l

def hasValues(l,n):
    has = 0
    for i in range(0,n+1):
        if(l[i] != 0):
            has = 1
    return has
            
def rango(l,m,n):
    r = 0
    for i in range(0,m):
        if(hasValues(l[i],n)):
            r += 1
    return r
    
def solution(rC,rA,n):
    if(rC != rA):
        return 'Ninguna Solución'
    if(rC == rA and rC == n):
        return 'Solución Unica'
    if(rC == rA and rC < n):
        return 'Infinidad de Soluciones'
    
def compact(l,m,n):
    for i in range(0,m):
        if(hasValues(l[i],n) == 0):
            l.remove(l[i])
    return l
    
