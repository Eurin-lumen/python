#-*-coding:Utf-8-*-
"""_summary_
# Exercice 6

    Écrire un programme qui demande un nombre de départ, et qui affiche les dix nombres suivants. Par exemple, si l'utilisateur entre le nombre 17, le programme affichera les nombres de 18 à 27.

"""
Nb = int(input("saisir un nombre : "))

for i in range(Nb, Nb + 10) :
    print(i)