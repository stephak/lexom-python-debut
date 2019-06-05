import csv

#méthode traditionnelle
path_file="squidAnonymise.log" #le fichier à lire, mis dans le repertoire par défaut.
fh = open(path_file,encoding='us-ascii')      # ouverture du fichier
reader = csv.reader(fh,delimiter=' ')   #le reader qui va permettre de le parcour, c est un 'iterable'


nb_lignes_parcourues = 0
nb_lignes_max=50

for ligne in reader:    #len est une liste
    nb_lignes_parcourues+=1
    print("nombre de colonnes de la ligne",nb_lignes_parcourues,"=",len(ligne))
    if nb_lignes_parcourues>nb_lignes_max:
        break
fh.close()

#méthode avec with
nb_lignes_parcourues = 0
nb_lignes_max=50
print("méthode avec with")
with open('squidAnonymise.log', encoding='us-ascii') as fh:
    reader = csv.reader(fh, delimiter=' ')
    for line in reader:
        nb_lignes_parcourues+=1
        print("nombre de colonnes de la ligne",nb_lignes_parcourues,"=",len(ligne))
        if nb_lignes_parcourues>nb_lignes_max:
            break