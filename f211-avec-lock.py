import random
import sys
import time
from threading import Thread, RLock
from humain import humain


lock = RLock()

class tache(Thread):
    """Thread chargé simplement d'afficher une lettre dans la console."""
    un_humain=''

    def __init__(self, nom):
        Thread.__init__(self)
        self.un_humain=humain(nom)

    def run(self):
        with lock:              #contexte manager pour bloquer le code
            self.un_humain.print_nom_vertical()




# Création des threads
thread_1 = tache("Stephane")
thread_2 = tache("Pierre")

# Lancement des threads
thread_1.start()
thread_2.start()

# Attend que les threads se terminent
thread_1.join()
thread_2.join()