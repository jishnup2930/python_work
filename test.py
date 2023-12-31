from postfix import evaluate

def test_single_operand():
    assert evaluate("5") == 5

def test_add():
    assert evaluate("62+") == 8

def test_substraction():
    assert evaluate("82-")==6

def test_substraction2():
    assert evaluate("25-")== -3

def test_multiplication():
    assert evaluate("22*")== 4

def test_division():
    assert evaluate("22/")==1