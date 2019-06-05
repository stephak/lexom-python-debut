#f22b.py
"""
    Bibliothèque de fonctions - on remarque la ligne vide dessous
    Bibliothèque de fonctions pour présenter des relations rigolottes en mathématique.
"""
from math import sqrt

def pythagore():
    """
        Fonction qui,  à la base d'un nombre entier proposé par l'utilisateur,
        affiche toutes les possibilités pour que la sommes de deux nombres au carré
        fasse ce nombre saisi au carré.

        :param arg1: aucun paramètre en entrée
        :return: dans le terminal, imprime les résultats

        :Example:

        >>>pythagore()
        "Maximum Number? "
        >>>4
        '3 ^2+ 4 ^2= 5 ^2'
    """

    n = input("Maximum Number? ")
    n = int(n) + 1
    for a in range(1, n):
        for b in range(a, n):
            c_square = a ** 2 + b ** 2
            c = int(sqrt(c_square))
            if (c_square - c ** 2) == 0:
                print(a,"^2+",b,"^2=",c, "^2")