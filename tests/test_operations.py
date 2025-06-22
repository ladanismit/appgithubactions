from src.math_operations import add,sub

def test_add():
    assert add(2,3)==5
    assert add(3,3)==6
    assert add(-2,3)==1
    assert add(10,3)==13

def test_sub():
    assert sub(5,3)==2
    assert sub(3,3)==0
    assert sub(2,3)==-1
    assert sub(10,3)==7

