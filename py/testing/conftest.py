import pytest
from test_models.user import User

@pytest.fixture
def mock_user():
  """A sample user on our platform"""
  return User("Dinesh", 25)