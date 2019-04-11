def additionner(a,b):
    return a + b

def test_additionner():
    assert additionner(3, 4) == 7
    assert additionner(-3, -9) == -12
    assert additionner(2.5, 2.5) == 5.0
