def add(a,b):
    return a+b

def test_add():
    assert add(2,3)==5
    assert add(-3,-5)==-8

def test_add_big_no():
    assert add(2000000,4000000)==6000000

# test method must start with test
