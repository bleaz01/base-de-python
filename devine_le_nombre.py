import random
chiffre = random.randint(0, 100)

reponse = None
liste = []



while reponse != chiffre:
    reponse = int(input("noté votre chiffre\n"))
    liste.append(reponse)

    if reponse < chiffre:
        print("le chiffre donné est plus petits que le chiffre secret")

    elif reponse > chiffre:
        print("le chiffre donné est plus grand que le chiffre secret")
    
    else:
        print("ta gagné")

nombre = len(liste)

for reponse, nombre in liste.items():
    print("vous avez reusi en ", nombre, "coup!")

