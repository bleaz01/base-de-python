def ajouter_4_a_liste(liste):

    liste.append(4)

    



    return liste

def test_ajouter_4_a_liste():
    assert ajouter_4_a_liste([5, 8, 6]) == [5, 8, 6, 4]
    assert ajouter_4_a_liste([6, 8]) == [6, 8, 4]
