from postfix import evaluate

def test_single_operand():
    assert evaluate("5") == 5

def test_add():
    assert evaluate("62+") == 8

def test_substraction():
    assert evaluate("82-")==6