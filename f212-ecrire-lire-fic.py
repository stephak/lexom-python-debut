import os

#création d'un fichier text
tab = ['vert', 'bleu', 'gris', 'jaune', 'rouge']
with open('test.txt','a') as f:
    for elt in tab:
        f.write(elt+'\n') #nécessaire de mettre le newline, il ne va pas de soit.

#on recupère les données sur le fichier
info=os.stat('test.txt')
print(type(info))
print(info)


#on supprime le fichier
os.remove('test.txt')