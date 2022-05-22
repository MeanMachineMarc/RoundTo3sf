import RoundTo3sf

def test_pos_integer():
    assert RoundTo3sf.round_3sf(3)==3

#def test_negative_integer():
 #   assert RoundTo3sf.round_3sf(-3)==-3

#def test_negative_float():
 #   assert RoundTo3sf.round_3sf(-3.3356)==-3.34

def test_positive_float():
    assert RoundTo3sf.round_3sf(3.3356)==3.34

def test_zero():
    assert RoundTo3sf.round_3sf(0)==0

def test_positive_many_dp():
    assert RoundTo3sf.round_3sf(0.003556)==0.00356

#def test_negative_many_dp():
#    assert RoundTo3sf.round_3sf(-0.003556)==-0.00356

