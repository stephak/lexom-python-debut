#f29-json.py
#On veut avoir le nombre de to do réalisé par utilisateur.
import json
import requests #il faut l'installer avant


a=[1,2,3,4,5]

response = requests.get("https://jsonplaceholder.typicode.com/todos")
todos = json.loads(response.text) #todos est une liste


#on va d'abord les parcourir un peu pour apprécier la magie du truc :
for elt in todos[0:10]:
    print(elt)

#le dictionnaire des clés user_id:nombre de to do completé que l'on veut obtenir
users_id_to_do_completed={0:0}

todos == response.json()

#après c'est juste une histoire de dictionnaire
for elt in todos:
    if elt["completed"]==True:
        if elt["userId"] in users_id_to_do_completed.keys():
            users_id_to_do_completed[elt["userId"]]=users_id_to_do_completed[elt["userId"]]+1
        else:
            users_id_to_do_completed[elt["userId"]]=1

print("ensemble des utilisateurs qui ont complété leur todo",users_id_to_do_completed)