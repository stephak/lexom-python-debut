import csv
import os
import subprocess
import datetime
import tarfile
import argparse

import sys

parser = argparse.ArgumentParser()

parser = argparse.ArgumentParser(description="Divers utilitaires pour la gestion de fichiers",prog='python utilitaires.py', usage='%(prog)s -d ./dev/ ou -t ./dev/..')
parser.add_argument('-d','--dstat', type=str,metavar='', help="renvoie le nombre de fichiers d\'un répertoire, la taille totale occupée et le plus gros fichier")
parser.add_argument('-c','--cpy',type=str, metavar='', help="compresse les *.py d'un repertoire")



args = parser.parse_args()

if len(sys.argv) < 2:
    parser.print_help()
    sys.exit(1)


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
        return 1
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

def tar_py(dir):
    """
    Permet de créer un tar compressé des fichiers *.py d'un repertoire


    :param dir: le repertoire mis en paramètre
    :return: création d'un tar dans le repertoire avec pour nom ddmmyyyy_pgm_py.tar
    """
    if not os.path.isdir(dir):
        print("repertoire ",dir,"non valide")
        return 1
    else :
        os.chdir(dir)
        nom_archive = datetime.datetime.now().strftime('%Y%m%d') + '-' + 'pgm.py.tar.gz'
        if os.name == 'posix  ':
            dirPy = subprocess.getstatusoutput("ls *.py")
            listPy=dirPy[1].split(os.linesep)
            with tarfile.open(nom_archive,'w:gz') as f:
                for elt in listPy:
                    f.add(elt)
        else :
            liste_fichiers = os.listdir()
            nb_fichiers = len(liste_fichiers)
            with tarfile.open(nom_archive,'w:gz') as f:
                for elt in liste_fichiers:
                    if elt[-3:]=='.py':
                        f.add(elt)

    return nom_archive


if args.dstat:
    print("---------------------------------")
    print("--Stats basiques sur répertoire--")
    print("---------------------------------")
    rep=args.dstat
    tmp=directory_stat(rep)
    if tmp != 1:
        print("Il y a ", tmp[1], "fichiers dans le repertoire",tmp[0])
        print("le plus gros est", tmp[3])

if  args.cpy:
    print("-------------------------------------")
    print("--Compression des programmes python--")
    print("-------------------------------------")
    rep = args.cpy
    tmp = tar_py(rep)
    if tmp != 1:
        print("Archive des py :",tmp)
