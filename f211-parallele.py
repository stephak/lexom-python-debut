#f211-parallele.py
import random
import sys
import time
from threading import Thread

def une_seule_tache(id):
    # Répète 20 fois
    i = 0
    while i < 20:
        print("thread",id,"A")
        attente = 0.2
        attente += random.randint(1, 60) / 100
        # attente est à présent entre 0.2 et 0.8
        time.sleep(attente)
        i += 1

class tache(Thread):
    """Thread chargé simplement d'afficher une lettre dans la console."""

    def __init__(self, id):
        Thread.__init__(self)
        self.id = id

    def run(self):
        une_seule_tache((self.id))


# Création des threads
thread_1 = tache(1)
thread_2 = tache(2)

# Lancement des threads
thread_1.start()
thread_2.start()