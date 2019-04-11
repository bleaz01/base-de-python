
def compter(start, stop, step): 
    x = start 
    resultat = ""
    while x <= stop:
        resultat = resultat + str(x)+"\n"
        x = x +step
     
    return resultat

def test_compter():
    assert compter(0,10,2)== "0\n2\n4\n6\n8\n10\n"
    assert compter(0,5,2) == "0\n2\n4\n"
