#-*-coding:Utf-8-*-
"""
Exercice 4
 
    Écrivez un programme qui lira au clavier l’heure et les minutes,et il affichera l’heure qu’il sera une minute plus tard. 
    Par exemple, si l'utilisateur tape 21 puis 32, l'algorithme doit répondre : "Dans une minute, il sera 21 heure(s) 33". 
    NB : on suppose que l'utilisateur entre une heure valide. 
    
    Pas besoin donc de la vérifier.

"""

heure = int(input("Saisir l'heure : "))
minutes = int(input("Saisir les minutes : "))
if heure < 23 : 
    if minutes == 59:
        heure+=1
        minutes=0
    else:
        minutes +=1
else:
    if minutes == 59:
        heure = 0
        minutes = 0
    else:
        minutes += 1
        