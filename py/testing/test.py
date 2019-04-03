'''why the hell
are you wring'''
class Tester:
  '''doc1'''
  def inc(self, ctype):
    return ctype + 1
    
  '''soc2'''
  def test_inc(self): 
    assert self.inc(3) == 4
    assert self.inc(2) == 3
    
    
  '''this will test'''
  @staticmethod
  def test_anything():
    assert 3 == 3

# t = Tester()
# t.test_inc()
# t.test_anything()

def add(a):
  def add1(b):
    def add2(c):
      return a + b + c
    return add2
  return add1

add_3_ = add(3)
add_3_4_ = add(3)(4)
it_adds_5_ = add(5)

print add(3)(4)(5)
print add_3_4_(5)
print add_3_(4)(5)
print add(5)(6)(7)
print it_adds_5_(6)(7)

print add
print add(3)
print add(3)(4)
print add(3)(4)(5)

def add(a, b, c):
  return a + b + c

import functools as fp
add_3_ = fp.partial(add, 3)
add_3_4 = fp.partial(add, 3, 4)
add_3_4_5 = fp.partial(add, 3, 4, 5)
print add_3_(4, 5)
print add_3_4_(5)
print add_3_4_5


# class Singy:
#   __INSTANCE = None

#   @classmethod
#   def getInstance(cls):
#     if not cls.__INSTANCE:
#       cls.__INSTANCE = Singy()
#     return cls.__INSTANCE
    
#   def __init__(self):
#     self.s = "from a singleton"
    
    
# x = Singy.getInstance()
# y = Singy.getInstance()
# z = Singy.getInstance()

# print x.s
# print y.s
# print z.s, '\n'

# x.s = x.s.upper()

# print x.s
# print y.s
# print z.s, '\n'

# z.s = z.s.lower()

# print x.s
# print y.s
# print z.s