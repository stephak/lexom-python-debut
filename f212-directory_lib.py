import csv
import os
import subprocess
import datetime
import tarfile

def a():
    nb_lignes_parcourues = 0
    with open('squidAnonymise.log', encoding='us-ascii') as fh:
        reader = csv.reader(fh, delimiter=' ')
        for line in reader:
            nb_lignes_parcourues+=1
        print(nb_lignes_parcourues)


def b():
    tab = ['vert', 'bleu', 'gris', 'jaune', 'rouge']
    with open('test.txt','a') as f:
        for elt in tab:
            f.write(elt+'\n')

def directory_stat(dir):
    """
    Statistiques basiques sur un repertoire
    Lister tous les fichiers d'un repertoire mis en paramètre, sortir le nombre de fichiers, la taille totale, le plus gros fichier
    le plus gros


    :arg string : le chemin d'un repertoire

    :return: un ensemble
        Le nom du répertoire mis en paramètre
        le nombre de fichiers dans le repertoire
        la taille totale
        le nom du fichier le plus gros, avec sa taille

    :example:

    >>>directory_stat(".")
    >>>('.', 32, 20824610, 'squidAnonymise.db(10354688)')

    """
    nb_fichiers=0
    taille_totale=0
    plus_gros=''
    taille_fichier_plus_gros=0
    if not os.path.isdir(dir):
        print("repertoire ",dir,"non valide")
        exit(1)
    else :
        os.chdir(dir)
        liste_fichiers=os.listdir()
        nb_fichiers=len(liste_fichiers)
        for fic in liste_fichiers:
            tmp=list(os.stat(fic)) #la taille du fichier est à l'enreguistrement numéro 6
            fic_size=int(tmp[6])
            if fic_size>taille_fichier_plus_gros:
                taille_fichier_plus_gros=fic_size
                plus_gros=fic + "(" +str(tmp[6]) +")"
            taille_totale+=tmp[6]
    return dir, nb_fichiers, taille_totale, plus_gros

if __name__ == "__main__":
    rep=os.getcwd()
    print("stat sur le repertoire en cours")
    print(directory_stat(rep))
