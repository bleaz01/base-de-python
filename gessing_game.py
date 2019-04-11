import random


print("tapé le numero\n")
guess = int(input())


nb_secret = random.randint(1,100)

while guess != nb_secret:
    if guess < nb_secret:
        print("ton nombre est inferieur")
    else:
        print("ton nombre est trop haute")
    print("recommance casse pas les couille")
    guess = int(input())


print("bravo, c'eatis bien le bon" +str(nb_secret) )

