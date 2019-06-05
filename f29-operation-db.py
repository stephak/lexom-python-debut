import sqlite3
path_db='laBelleGodasse.db'
conn=sqlite3.connect(path_db)  #connexion à la base de données
c=conn.cursor()    


#peu de données, une suels fois
c.execute('select * from magasins')
selections=c.fetchall() #on met tout dans une liste (chaque éléments de la liste selections est une ligne )
for ligne in selections:
    print(ligne[0],ligne[1],ligne[2])

#bcp de données


#execution d'une commande sql
sql="insert into magasins values(5,\"1 Bd des champs Elysées\",\"75000 Paris\ ») »
c.execute(sql)

c.commit()
c.close()