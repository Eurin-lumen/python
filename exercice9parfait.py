def est_parfait(n):
        somme_diviseurs = 1 #on commence à 1 car on ne le testera pas mais il est toujours diviseur
        for i in range(2, round(n**0.5)+1): #on teste tous les entiers de 2 jusqu'à racine de n comprise
                #comme les diviseurs vont par pair, cela permet de simplifier les calculs
                if n%i == 0: #si i est un diviseur de n
                        somme_diviseurs += i #on ajoute i à la somme
                        somme_diviseurs += n/i #on ajoute n/i, qui est aussi un diviseur de n
        if n == somme_diviseurs :
                return True
        else :
                return False