#-*-coding:Utf-8-*-

"""_summary_
# Exercice 7

    Le pgcd de deux nombres par soustractions successives.
    pgcd (a, b)= pgcd (a moins b, a) si a> b
    pgcd (a, b)= pgcd (a,b moins a) si b >a
    pgcd (a, b)= a si a = b
    On suppose que les opérandes sont des entiers positifs, écrire un programme qui permet de calculer le PGCD de deux nombres a et b.


"""
from tkinter import *
from tkinter import ttk
from tkinter import N


a = int(input("Saisir le premier nombre : "))
b = int (input("saisir le deuxième nombre : "))

n = a
m = b

while n != m:
    if n > m:
        n,m = (n-m),n
    elif n < m:
        n,m = n, (m,n)
print("Le PGCD de {a} et de {b} est : {n}")
    