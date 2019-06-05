""""
   Bibliothèque pour représenter une personne et des informations basiques
"""
import datetime



class Personne:
    nom=''
    prenom=''
    dob=''

    def __init__(self, *args, nom='', prenom='', dob='01/01/1900'):
        self.nom=nom
        self.prenom=prenom
        self.dob=dob

    def age(self):
        tmp=self.dob.split('/') #on met la date dans un tableau pour en isoler les composants
        t_dob=datetime.date(int(tmp[2]),int(tmp[1]),int(tmp[0]), ) #ainsi on a la date au format date
        ajd = datetime.date.today()

        nb_jours_an = 365.2425
        v = int((ajd - t_dob).days / nb_jours_an)
        return v
