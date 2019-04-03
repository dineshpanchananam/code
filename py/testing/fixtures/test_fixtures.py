import pytest 

def test_user(mock_user):
  assert mock_user.age == 25
  assert mock_user.name == "Dinesh"