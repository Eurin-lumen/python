
from math import *
N = int(input("Saisir un nombre : "))
S = 0
for i in range(2, ceil(sqrt(N)) +1):
    if N%i == 0:
        S+=i
        
if S == N:
    print(f"{N} est un nombre parfait")
    
    