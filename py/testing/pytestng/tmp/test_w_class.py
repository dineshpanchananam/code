import pytest

class TestONo:
  
  @pytest.mark.special
  def test_xyz(self):
    assert [] == list()
  
  @pytest.mark.feature
  @pytest.mark.skip
  def test_iop(self):
    pass
  
  @pytest.mark.skip
  def test_zde(self):
    with pytest.raises(ZeroDivisionError):
      1 / 0.1
      
@pytest.mark.feature
class TestBOne:
  
  def test_wth(self):
    pass

  def test(self):
    pass