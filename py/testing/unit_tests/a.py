from __future__ import absolute_import
from __future__ import print_function
from __future__ import division
import unittest

class Q(unittest.TestCase):
  def inc(self, x):
    return x + 1
  
  def decr(self, x):
    return x - 1

  def test(self):
    self.assertEquals(self.inc(3), 4)

  def test_decr(self):
    self.assertEquals(self.inc(3), 4)

  def test_same(self):
    print(self.assertEqual, end='')
    print(self.assertEquals)
    self.assertEquals(4, 4.0)
    x = 7 / 3
    print(x)

if __name__ == "__main__":
  unittest.main()