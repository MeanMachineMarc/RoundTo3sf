import Sign

def test_positive():
    assert Sign.sign(3)==1

def test_negative():
    assert Sign.sign(-3)==-1

def test_zero():
    assert Sign.sign(0)==0