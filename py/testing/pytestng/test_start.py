from mock import Mock, patch
import pytest

def abfg():
  return "abcdefg"

def test_abfg(snapshot):
	snapshot.assert_match(abfg())

@pytest.mark.parametrize("input_,output",
[ ('1+2', 3),
  ('2-3', -1),
  ('10+10', 20),
  ('3-3', 0),
  ('4+5', 10-1)])
def test_func(input_, output):
  assert eval(input_) == output
  
def max_trip(x):
  return sorted(x)[-1]
  
@pytest.mark.parametrize("inp, out",
[ ([2, 3, 4], 4),
  ([5], 5),
  ([6, -5], 6)]  
)
def test_max_trip(inp, out):
  assert max_trip(inp) == out

class TestXYZ:
  def test_cvb(this):
    assert len([]) == 0
  
  def gcd(self, a, b):
    return self.gcd(b, a % b) if b else a
    
  @pytest.mark.skip
  def test_spec(this):
    assert 11 == this.gcd(30, 10)
    
  def test_err(self):
    with pytest.raises(ZeroDivisionError):
      1 / 0
  
def inf():
  inf()

def test_rec_depth():
  with pytest.raises(RuntimeError, match="recursion") as re:
    inf()
    
@pytest.mark.skip
def test_set_equality():
  assert set("dabc") == set("bcd")

def abcd(svc, value):
  ret = svc.call(value)
  return abs(ret)

@pytest.mark.parametrize('param, expected', [
  (5, 5),
  (-4, 4),
  (-3, 3),
  (4, 4)
])
def test_abcd(param, expected):
  mocksvc = Mock()
  mocksvc.call.return_value =  param
  actual = abcd(mocksvc, param)
  assert actual == expected