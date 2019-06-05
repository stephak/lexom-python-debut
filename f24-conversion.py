def convertir_entier(a):
    try:
        return True, int(a)
    except:
        return False, "Banane, c'est pas un entier"

while True:
    print("donnez un nombre")
    a,b=convertir_entier(input())
    if a==True:
        print(b*b)
    else:
        print(b)