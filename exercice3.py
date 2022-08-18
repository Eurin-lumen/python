#-*-coding:Utf-8-*-

"""
Exercice 3
Ecrire un programme qui permet de calculer le montant des heures supplémentaires d’un employé, sachant le prix unitaire d’une heure selon lebarème suivant :
    • Les 39 premières heures sans supplément,
    • De la 40ième à la 44ième heure sont majorées de 50%,
    • De la 45ième à la 49ième heure sont majorées de 75%,
    • De la 50ième heure ou plus, sont majorées de 100%.


"""
nombreHeures = int(input("saisir le nombre d'heures : "))
prix = float(input("saisir le prix unitaire d'une heure "))
montant = 0

if nombreHeures <= 39: 
    montant = 0
elif nombreHeures < 45 :
    montant = (nombreHeures - 39) * (prix * 1.5)
elif nombreHeures < 50 :
    montant= (5 * prix * 1.5) + (nombreHeures - 44 ) * (prix * 1.75)
else:
    montant= (5 * prix * 1.5 ) + (5 * prix * 1.75 ) + (nombreHeures - 49) * (prix * 2)
print(f"Le montant des heures supplémentaires est  :  {montant} ")