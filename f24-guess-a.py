#f24-guess-a.py
nb_a_trouver=17
print("deviner le nombre compris entre 0 et 100")
nbTest=0
test=False
while test==False:
    print("proposition...")
    i=int(input()) #permet de saisir un nombre au clavier
    if i>nb_a_trouver:
        print("trop grand")
    elif i<nb_a_trouver:
        print("trop petit")
    elif i==nb_a_trouver:
        test=True
        print("bravo")