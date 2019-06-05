#f24-diviser-entier.py

def diviser_entier(a,b):
    try:
        a=int(a)
        if (a<0 or a>100):
            raise(ValueError)
        b=int(b)
        return True, a/b
    except ValueError:
        print("ValueError")
        return False, "Banane, tu as un problème sur la valeur en entrée"
    except ZeroDivisionError:
        print("ZeroDivisionError")
        return False, "Banane, ty peux pas divisier un nombre par 0"
    except TypeError: #ne doit pas arriver car ce qui vient en input est juste du string
        print("TypeError")
        return False, "Banane, tu as un problème sur le type en entrée"
    finally:
        print("je passe par là dans tous les cas")
        
while True:
  a=input()
  b=input()
  print("le résultat de la division de %d par %s est",a,b)
  print(diviser_entier(a,b))