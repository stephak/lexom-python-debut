#f22a.py
# je mets un commentaire
from math import sqrt

n = input("Maximum Number? ")
n = int(n) + 1
for a in range(1, n):
    for b in range(a, n):
        c_square = a ** 2 + b ** 2
        c = int(sqrt(c_square))
        if (c_square - c ** 2) == 0:
            print(a,"^2+",b,"^2=",c,"^2")