#creation d'une base de données pour insertions des données 'transaction Magazin'
#attentio le fichier est en utf-8
#1,Rennes,30/03/2018,H,Chaussures de sport,46.0,60
#2,Rennes,15/09/2018,E,Bottes,30.5,40
#3,Dinan,22/09/2018,E,Baskets,24.0,120
#4,Rennes,01/12/2018,H,Baskets,43.0,60
#5,Rennes,18/01/2018,F,Chaussures à lacets,32.5,40
#6,Rennes,26/05/2018,E,Bottes,26.0,120
#7,Rennes,13/10/2018,F,Mules et sabots,40.0,40
#8,Saint Brieuc,10/02/2018,F,Baskets,33.0,40

#dans le mmodèle en trois tables
import sqlite3
import os
import csv

#on veut créer la base de données dans le même répertoire que le programme
#dans ce repertoire on a aussi le fichier à charger
dir_path = os.path.dirname(os.path.realpath(__file__)) #récupper le répertoire courant
os.chdir(dir_path) #on execute le programme dans ce répertoire, ça permet d'avoir tout au même endroit
try :
    os.remove('laBelleGodasse.db')
except:
    print("le fichier ",'laBelleGodasse.db',"n'existe pas")
conn=sqlite3.connect('laBelleGodasse.db')

#créer la base
c=conn.cursor()
c.execute('''create table MAGASINS(id_magasin int primary key,adresse char, ville char)''')
c.execute('''create table MODELES(id_modeles int primary key,genre char, type char, prix int)''')
c.execute('''create table TRANSACTIONS(id_transaction int primary key, id_magasin int, id_modele int, pointure char, date_transaction char, FOREIGN KEY (id_magasin) REFERENCES MAGASIN(id_magasin),FOREIGN KEY (id_modele ) REFERENCES MODELE(id_modele) )''')


#on remplit la base en parcourant le fichier
liste_magasins=[]
liste_modeles=[]
i=0
with open('f29-transactions-magasins.txt' ) as f:
    reader = csv.reader(f,delimiter=',')
    for row in reader:
            if i%1000==0:
                print(i,"lignes parcourues")
                conn.commit() #toutes les 1000 lignes on fait un commit
            i+=1
            id_ec=row[0] #ec signifie 'en cours'
            ville_ec=row[1]
            date_ec=row[2]
            genre_ec=row[3]
            type_ec=row[4]
            pointure_ec=row[5]
            prix_ec=row[6]
            #on va mettre les magasins (ville) et les modèles dans des listes de manière à avoir des numéros qui serviront de clés
            if ville_ec not in liste_magasins :
                liste_magasins.append(ville_ec)
                req_mag='insert into MAGASINS values ('+str(liste_magasins.index(ville_ec))+',"","'+ville_ec+'")'
                #print(req_mag)
                c.execute(req_mag)
            
            #un modele est défini par l'unicité du genre, du type et du prix, c'est donc notre clé primaire pour la liste modele
            keyModele=genre_ec+type_ec+prix_ec
            if keyModele not in liste_modeles :
                liste_modeles.append(keyModele)  
                req_model='insert into MODELES values ('+str(liste_modeles.index(keyModele))+',"'+genre_ec+'","'+type_ec+'",'+prix_ec+')'
                #print(req_model)
                c.execute(req_model)
                
            #on fait l'insertion dans les tables
            req_transaction='insert into TRANSACTIONS values ('+str(i)+','+str(liste_magasins.index(ville_ec))+','+str(liste_modeles.index(keyModele))+',"'+pointure_ec+'","'+date_ec+'")'
            #print(req_transaction)
            c.execute(req_transaction)
            
            
            
conn.commit() #pour les milles dernières lignes            
#on met les contraintes
#clés primaires

#clés étrangères

conn.close()










