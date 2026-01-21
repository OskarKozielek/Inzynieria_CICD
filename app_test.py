from app import add, sub

def test_add():
  assert add(4,2) == 6

def test_sub():
  assert sub(4, 3) == 1
