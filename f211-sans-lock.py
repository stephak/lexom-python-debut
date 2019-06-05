from threading import Thread,RLock
from humain import humain


#on imprime les noms verticaux sequentiellement, l'un après l'autre

print("Impression sequentielle")
pierre=humain("Pierre")
pierre.print_nom_vertical()

stephane=humain("Stephane")
stephane.print_nom_vertical()


print("Impression dans des threads, sans lock")

#on lance les process d'impression en même temps
class tache1(Thread):
    """Thread chargé simplement d'afficher les noms"""
    un_humain=''

    def __init__(self, nom):
        Thread.__init__(self)
        self.un_humain=humain(nom)

    def run(self):
        self.un_humain.print_nom_vertical()

# Création des threads
thread_1 = tache1("Stephane")
thread_2 = tache1("Pierre")

# Lancement des threads
thread_1.start()
thread_2.start()
