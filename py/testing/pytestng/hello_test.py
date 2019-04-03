import pytest 

def inc(x):
  return x + 1

def test_inc():
  assert 4 == inc(3)
  assert -3 == inc(-4)

def test_has_attr():
  assert hasattr(int, 'imag')
  assert hasattr('34', 'upper')
  assert hasattr('', '__class__')
  # assert hasattr('', 'to_int')
  
def get_countries():
  return ['India', 'USA']
  
@pytest.mark.skip
def test_countries(snapshot):
  snapshot.assert_match(get_countries())
  
@pytest.mark.tmpdir
def test_tmpdir(tmpdir,):
  print (tmpdir)
  assert 1