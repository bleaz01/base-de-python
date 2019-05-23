
reponse = None
couleur = {} 

while reponse != " ":
    reponse = input(" noté votre couleur·\n")

    if reponse:
        
        if reponse in couleur: 
                couleur[reponse] = couleur[reponse] + 1
        else:
            couleur[reponse] = 1

print("les vote sont ")
for couleur, resultat in reponse.items():
    print('-' , couleur, ";",  resultat)
