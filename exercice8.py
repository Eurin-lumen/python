
from tkinter import N


N = int(input("Saisir un nombre  :"))
S = 0
for i in range(N):
    nb = int(input("saisir un nombre : "))
    S+=nb
    break
M = S/N
print(f"La somme est  {S} et la moyenne est {M}")