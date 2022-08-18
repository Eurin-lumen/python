#-*-coding:Utf-8-*-

"""
Exercice 2
Ecrire un programme qui demande deux nombres à l’utilisateur etl’informe ensuite si leur produit est négatif ou positif. Attention toutefois :on ne doit pas calculer le produit des deux nombres.
"""

a = int(input("Saisir un nombre [a]: "))
b = int(input("Saisir un nombre [b]: "))

if a > 0 and b > 0 or a < 0 and b < 0 :
    print("Le produit est positif")
else :
    print("Le produit est négatif")