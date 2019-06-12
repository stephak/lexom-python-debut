#f29_pandas.py
import pandas as pd

a=[1,2,3,4,

df = pd.read_csv ('popCommune2015.csv', sep=";")
#print (df)

#comptage de valeurs non vides
print(df.count())

#on change le dataFrame pour rajouter une colonne calclulée à partir de la population
err=''
popu=[]
for index,row in df.iterrows():
    nb=row["Population totale"]
    try:
        nbi=int(str(nb).replace(' ',''))
        #row["pop"]=nbi
        popu.append(nbi)
    except:
        err=err+nb+';'
        popu.append(0)

#passage intéressant : on rajoute une colonne ("pop") qu'on initialise à partir d'une liste (vecteur)
df["pop"]=popu

#on crée un dataframe qui est un sous ensemble
df2=df[["Code région","Code département","pop"]]

#description du fichier
print(df.columns)


groupby_sum1 = df2[["Code région","pop"]].groupby(["Code région"]).sum() 
groupby_sum2 = df2[["Code département","pop"]].groupby(["Code département"]).sum() 

# block 1 - simple stats
mean1 = df2["pop"].mean()
sum1 = df2['pop'].sum()
max1 = df2['pop'].max()
min1 = df2['pop'].min()
count1 = df2['pop'].count()
median1 = df2['pop'].median() 
std1 = df2['pop'].std() 
var1 = df2['pop'].var()  


# print block 1
print ('Moyenne de population ' + str(mean1))
print ('Somme des populations: ' + str(sum1))
print ('Max de population: ' + str(max1))
print ('Min de population: ' + str(min1))
print ('Nomnbe de communes: ' + str(count1))
print ('Mediane de population: ' + str(median1))
print ('Ecart type de population: ' + str(std1))
print ('variance de la population ' + str(var1))

print ('groupe by région ' + str(groupby_sum1))
print ('group by departement: ' + str(groupby_sum2))