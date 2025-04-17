from src.math_operations import add,sub

def test_add():
    assert add(2,3)==5
    assert add(1,3)==4

def test_sub():
    assert sub(4,3)==1
    assert sub(7,4)==3
    assert sub(8,9)==-1
    
