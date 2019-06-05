import sqlite3
import os
import csv
import datetime

path = "/Users/stephanehak.ni/dev/lexom-python-lille"
file = "squidAnonymise.log"
db = "squidAnonymise.db"
path_file = path + os.sep + file
path_db = path + os.sep + db


def clean_str(tmp):
    """ Dans une chaine, remplace plusieurs espaces concomittants par un seul

    :param arg1: une chaine contenant un ou plusieurs espaces en guise de séparation de champs
    :return : une chaine ne contenant qu'un espace entre chaque champs


    :Example:

    >>>from lire_log import clean_str
    >>>clean_str(\"111      BBBB   ijou  jjjj\")
    >>>\"111 BBBB ijou jjjj\"
    """

    tmp = str(tmp).replace("'", """""")  # pour supprimer les cotes qui vont poser un pb l'insertion en sql
    t1 = str(tmp).split(' ')
    t2 = []
    for l in t1:  # on supprime les ' ' en trops
        if l != '':
            t2.append(l)

    tmp2 = " ".join(t2)  # on transforme la liste en chaine propre en concatenant les éléments avec séparation " "
    return tmp2


def convert_epoch(d):
    """ converti une date epoch en date calendrier
    1555279207.109

    :param arg1: chaine de caractère représentant un epoch


    :return : une chaine de caractères représentant une date au format YYYY-MM-DD HH:MM:SS.SSS
              qui est le format par défaut sqllite.

    :Example:
    >>>convert_epoch("1555279207.109")
    >>>datetime.datetime(2019, 4, 15, 0, 0, 7, 109000)
    """
    try:
        d = float(d)
    except:
        d = 0  # on met la date à 0, qui sera convertie en 1 janvier 1970

    tmp = datetime.datetime.fromtimestamp(float(d)).strftime("%Y-%m-%d %H:%M:%S.%f")

    return tmp


sql_table_request = "create table REQUESTS (" \
                    "request_date date," \
                    "duration int," \
                    "client_address char," \
                    "result_codes char," \
                    "reply_size char," \
                    "request_method char," \
                    "reques_url char," \
                    "user char," \
                    "hierarchy_code char," \
                    "request_mime_type char," \
                    "request_ip_accepted char," \
                    "request_named_header char" \
                    ")"


def create_db(path=path, file=file):
    path_file = path + os.path + file  # chemin absolu du fichier
    # On crée la base
    db = file.split(('.'))[0] + '.db'  # le nom de la base de données est le même que le nom du fichier
    path_db = path + os.path.sep + db
    # création d'une base de données (c'est un seul fichier sqllite) qui sera utiliée \
    # pour les seuls besoins d'analyse, en local.
    try:
        os.remove(path_db)
    except:
        print("le fichier ", db, "n'existe pas, on le crée")

    conn = sqlite3.connect(path_db)
    c = conn.cursor()
    c.execute(sql_table_request)

    nombre_de_colonnes = set({})  # On va parcourir le fichier texte, on va vérifier
    # que toutes les lignes ont le même nombre de colonnes
    # C'est un petit test de data qaulity. ON va parcourir le
    # fichier et pour chaque ligne mettre le nombre de colonne obtenues
    # dans un ensemble (set) qui ne peut contenir que des valeurs uniques.

    fh = open(path_file)
    reader = csv.reader(fh)
    nb_lignes_max = 100000
    nb_lignes_lues = 0
    for ligne in reader:  # attention ligne est une liste car csv normalement separé par virgule
        nb_lignes_lues += 1
        if nb_lignes_lues > nb_lignes_max:
            break
        ligne_propre = clean_str(ligne[0])

        tab = str(ligne_propre).split(' ')

        nombre_de_colonnes.add(
            len(tab))  # pour avoir le nombre de colonnes et vérifier qu'il n'y ait pas de différences

        tab[0] = convert_epoch(tab[0])  # on met une date dans le premier champs
        sql_tmp = ""
        for elt in tab:
            sql_tmp = sql_tmp + "','" + elt
        sql_tmp = sql_tmp[2:] + '\''  # pour supprimer les deux premiers caractères dus à la construction de sql_tmp

        sql = "insert into REQUESTS values (" + sql_tmp + ")"
        try:
            c.execute(sql)
        except:
            print("erreur sur ligne: ", nb_lignes_lues, sql)

    conn.commit()
    conn.close()
    print("Nombre de colonnes : ",
          nombre_de_colonnes)  # on voir au passage la facilité du truc, on imprime un tableau là


def get_weird_queries(path, db, nb_lignes):
    """renvoie une liste des requetes les plus longues

    :param nb_lignes : nombre de lignes que l'on veut voir
    :return un liste de nb_lignes requetes les plus longues
    """
    path_db = path + os.path.sep + db
    conn = sqlite3.connect(path_db)
    c = conn.cursor()

    l = []

    nb_lignes_lues = 0
    sql_tmp = "select * from requests order by duration desc"
    c.execute(sql_tmp)
    while (1):
        row = c.fetchone()  # on parcours le select ligne par ligne
        if row == None or nb_lignes_lues >= nb_lignes_a_voir:
            break
        l.append(row)

    nb_lignes_lues += 1
    conn.close()
    return l

if __name__ == '__main__':
    create_db(path,file)
