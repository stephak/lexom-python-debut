import csv

path_file='squidAnonymise.log' #le fichier à lire, mis dans le repertoire par défaut.
fh = open(path_file,encoding='us-ascii')      # ouverture du fichier
reader = csv.reader(fh)   #le reader qui va permettre de le parcour, c'est un 'iterable'