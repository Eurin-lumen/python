# Python code to demonstrate the working of gcd()
# importing "math" for mathematical operations
import math
a = int(input("Saisir le premier nombre : "))
b = int (input("saisir le deuxième nombre : "))
         
print(f"Le PGCD de {a} et {b} est : ", end="")
print(math.gcd(a, b))