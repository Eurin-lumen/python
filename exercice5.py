#-*-coding:Utf-8-*-
"""
Exercice 5
 
    Écrire un programme qui à partir d’une note affiche la mention correspondant ?  
"""
note = float(input("saissisez une note : "))
if note < 10 :
    print("Non Admis")
elif note < 12 :
    print("passable")
elif note < 14 :
    print ("assez-bien")
elif note < 16 :
    print("bien")
elif note <= 20:
    print("Très bien ")
else :
    print("Saisir une note valide ")