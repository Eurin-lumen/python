#-*-coding:Utf-8-*-
"""
Exercice 1
Ecrire un programme qui permet de saisir un nombre puis déterminer s’il appartient à un intervalle donné, sachant que les extrémités del’intervalle sont fixées par l’utilisateur.

"""
a = int(input("Saisir [a : "))
b = int(input("Saisir  b] : "))

val = int(input("Saisir une valeur : "))
if a <= val <= b :
    print(f"{val} appartient à l'intervalle [{a} ; {b} ]")
else:
    print(f"{val} n'appartient pas à l'intervalle [{a} ; {b} ]")
