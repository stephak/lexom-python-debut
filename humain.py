import random
import time

class mammifere():
    nom=''
    sommeil={}          #tous les mamifères dorment
    def __init__(self,nom):
        self.nom=nom

    def dormir(self,date,heure_sommeil):
        self.sommeil[date]=heure_sommeil

    def totalSommeil(self):
        total=0
        for val in self.sommeil.values():
            total+=val
        return total

    def print(self):
        print(self.nom)
        for key,value in self.sommeil.items():
            print("le ",key, value,"heures de sommeil")


class humain(mammifere):  #héritage, humain hérite de mamifère.
    diplome=[]           #un attribut que n'ont pas tous les mamifères

    def __init__(self, nom):
        mammifere.__init__(self, nom)

    def add_diplome(self,dipl):
        self.diplome.append(dipl)

    def print_diplome(self):
        for elt in self.diplome:
            print(elt)

    def print(self):
        mammifere.print(self)
        print(self.diplome)

    def joue_aux_des(self):
        des=[]
        for i in [1,2,3]:
            des.append(random.randint(1,6))

        return des

    def print_jeux_de_des(self):
        print(self.nom,'a joué',self.joue_aux_des())

    def print_nom_vertical(self):
        #attente = 0.01
        for i in self.nom:
            attente = random.randint(1, 60) / 300
            time.sleep(attente)
            print(i)

if __name__=="__main__":
    Luigi = mammifere("Luigi")

    Luigi.dormir("22042019", 10)
    Luigi.dormir("23042019", 8)
    Luigi.dormir("24042019", 7)
    Luigi.print()

    print(Luigi.totalSommeil())

    pierre=humain("Pierre")
    pierre.add_diplome("DUT Mécanique")
    pierre.add_diplome("MASTER Histoire des arts")
    pierre.add_diplome("Permis de conduire")
    pierre.print_diplome()

    pierre.dormir("22042019", 9)
    pierre.dormir("22042018", 7)
    pierre.dormir("22042017", 5)
    pierre.dormir("22042016", 6)

    print(pierre.totalSommeil())
    pierre.print()

    pierre.print_jeux_de_des()


    pierre.print_nom_vertical()


