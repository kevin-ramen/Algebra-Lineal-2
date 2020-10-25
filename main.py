# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 10:15:01 2020

@author: kevin
"""
import gauss as gs
import auxclass as aux
import sys

print("\n-------------Calculadora de Sistemas de Ecuaciones MxN-------------\nIngresa el numero de Ecuaciones: ")
m = int(input())#Ecuaciones
print("Ingresa el numero de incognitas: ")
n = int(input())#Incognitas
l= aux.strlist(m)#inicializa la lista
l = aux.add(l,m,n)#Lista de Listas que contiene las ecuaciones
print("-----------Matriz del Sistema "+str(m)+"x"+str(n)+"-----------")
aux.printMatrix(l,m)#Imprimir la matriz

#Diagonalizacion y Teorema de Rouche-Frobenius
l = gs.Diagonalize(l,m,n)
print("-----------Matriz de Coeficientes Diagonalizada-----------")
aux.printMatrixCoe(l,m,n)
print("-----------Matriz Aumentada Diagonalizada-----------")
aux.printMatrix(l,m)
rC = gs.rango(l,m,n-1)#Rango de la matriz de coeficientes
rA = gs.rango(l,m,n)#Rango de la matriz aumentada
sol = gs.solution(rC,rA,n)#solucion string
print("\nR(A) =",rC)
print("R(A*) =",rA)
print("n =",n)
print("\nPor lo tanto el Sistema tiene: ", sol, "\n")
if(gs.isHomogeneous(l,m,n)):#Caso particular
    print("Es Homogenea\n")

if(sol == 'Ninguna Solución'):
    sys.exit(0)#Finaliza el programa
"""
#Reduccion de Gauss-Jordan
print("-----------Matriz por Llevar a su forma escalonada-----------")
l = gs.compact(l,m,n)
m = len(l)
aux.printMatrix(l,m)
#Resultado
"""    