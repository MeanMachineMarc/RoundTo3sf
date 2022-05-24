import pytest
import RoundTo3sf

def test_pos_integer():
    assert RoundTo3sf.round_3sf(3)==3

def test_negative_integer():
    assert RoundTo3sf.round_3sf(-3)==-3

def test_negative_float():
    assert RoundTo3sf.round_3sf(-3.3356)==-3.34

def test_positive_float():
    assert RoundTo3sf.round_3sf(3.3356)==3.34

def test_zero():
    assert RoundTo3sf.round_3sf(0)==0

def test_positive_many_dp():
    assert RoundTo3sf.round_3sf(0.006356)==0.00636

def test_negative_many_dp():
    assert RoundTo3sf.round_3sf(-0.006356)==-0.00636

def test_negative_float2():
    assert RoundTo3sf.round_3sf(-33.36)==-33.4

def test_positive_float2():
    assert RoundTo3sf.round_3sf(33.36)==33.4

def test_string_input_fail():
    with pytest.raises(Exception) as e_info:
         RoundTo3sf.round_3sf('egged')==-33.4

def test_empty_string_fail():
    with pytest.raises(Exception) as e_info:
         RoundTo3sf.round_3sf('')==-33.4

def test_no_input_fail():
    with pytest.raises(Exception) as e_info:
         RoundTo3sf.round_3sf()==-33.4