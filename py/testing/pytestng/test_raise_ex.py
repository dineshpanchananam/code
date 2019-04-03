import pytest

def hello():
  raise ValueError("abcd")

def test_hello():
  with pytest.raises(ValueError):
    hello()