from calculator import Calculator

def test_add() :
    calc = Calculator()

    assert calc.add(1, 2) == 3

    assert calc.add(0, 0) == 0

    assert calc.add(-1, 1) == 0

def test_sub() :
    calc = Calculator()

    assert calc.sub(2,1) == 1

    assert calc.sub(5, 2) == 3

    assert calc.sub(10, 5) == 5

def test_division() :

    calc = Calculator()

    try:

        calc.division(5,0)

    except ValueError as e :

        assert str(e) == "Cannot divide by zero"

    assert calc.division(10,2) == 5

    assert calc.division(15, 2) == 7.5

    assert calc.division(10, 5) == 2

def test_multiplication() :
    calc = Calculator()

    assert calc.multiplication(11,2) == 22

    assert calc.multiplication(20, 2) == 40

    assert calc.multiplication(8, 2) == 16




