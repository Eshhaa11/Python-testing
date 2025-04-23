def test_add() :

    assert add(1, 2) == 3

    assert add(0, 0) ==0

    assert add(-1, 1) == 0

def add(a,b):
    return a + b


def test_sub() :
    assert sub(1, 2) == -1

    assert sub(0, 0) == 0

    assert sub(1, 1) == 0

def sub(a,b):
    return a - b

def test_multiplication() :

    assert multiplication(2, 2) == 4

    assert multiplication(10, 4) == 40

    assert multiplication(15, 2) == 30

def multiplication(a,b):
    return a * b


def test_division() :
    assert division(10, 4) == 2.5

    assert division(25, 5) == 5

    assert division(28, 2) == 14

def division(a,b):
    return a / b


