#f211-parallele-2.py
import random
import sys
import time
from threading import Thread
from humain import humain



class tache(Thread):
    """Thread chargé simplement d'afficher une lettre dans la console."""
    un_humain=''

    def __init__(self, nom):
        Thread.__init__(self)
        self.un_humain=humain(nom)

    def run(self):
        attente = 0.2
        for i in range(1,10):
            attente += random.randint(1, 60) / 100
            time.sleep(attente)
            self.un_humain.print_jeux_de_des()




# Création des threads
thread_1 = tache("Stephane")
thread_2 = tache("Pierre")

# Lancement des threads
thread_1.start()
thread_2.start()