import pytest
from test_models.user import User

@pytest.mark.functional
def test_b():
  assert 1 == 1.0
  
@pytest.mark.perf
def test_cvb():
  assert 0 == False
  
def test_mock_user(
  mock_user,
  mock_user_session, 
  mock_user_class,
  mock_user_module):
  pass