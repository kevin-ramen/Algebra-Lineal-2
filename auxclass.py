# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 11:40:13 2020

@author: kevin
"""
def strlist(m):
    s=[]
    for i in range(0, m):
        s.append("l"+str(i))
    return s

def add(l,m,n):
    for i in range(0,m):#Ecuacion
        print("\nEcuacion",i+1)
        l[i]=[]
        for j in range(0,n+1):#Incognita
            if(j == n):
                print("Ingrese el Coeficiente de B"+str(i+1))
            else:
                print("Ingrese el Coeficiente de X"+str(j+1))
            l[i].append(float(input()))
    return l

def printMatrix(l,m):
    for i in range(0,m):
        print(l[i])

def printMatrixCoe(l,m,n):
    for i in range(0,m):
        print("[",end="")
        for j in range(n):
            if(j==n-1):
                print(l[i][j],end="")
            else:
                print(l[i][j],", ",end="")
        print("]")

def auxList(l,m,n,pos):
    lt = []
    for i in range(0,n+1):
        lt.append(l[pos][i])
    return lt

def copy(l,m):
    lt = []
    for i in range(0,m):
        lt.append(l[i])
    return lt

    