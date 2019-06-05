#f24-guess-b.py
import random
nb_a_trouver=random.randint(1,100)
print("deviner le nombre compris entre 0 et 100 en moins de 10 coups")
nb_test=0
test=False
while test==False:
    print("proposition...")
    i=int(input()) #permet de saisir un nombre au clavier
    nb_test+=1
    if nb_test>=10:
        print("perdu, plus de 10 coups")
        break
    if i>nb_a_trouver:
        print("trop grand")
    elif i<nb_a_trouver:
        print("trop petit")
    elif i==nb_a_trouver:
        test=True
        print("bravo, trouvé en",nb_test,"coups" )