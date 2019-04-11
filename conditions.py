reponse = input("quel points avez vous\n")
reponse1 =input("votre nom\n")
points = int(reponse)
personne= (reponse1)
def grade(points):

    if  points >= 18:
        return ("bonjour "+ personne +"vous avez "+"la plus grande distinction")
    elif points >=16:
        return ("bonjour "+ personne  +"grand distinction")
    elif points >= 14:
        return "distinction"
    elif points >= 12:
        return "satifaction"
    else:
        return "ajourné"

        



def test_grade():
    assert points(16)== "la plus grande distinction"


print(grade(points))


