class Abc:
  def add(self, a1, a2):
    print(self.__class__)
    return a1 + a2
  
  @staticmethod
  def add1(a1, a2):
    print(Abc.__class__)
    return a1 + a2
  
  @classmethod
  def add2(cls, a1, a2):
    print(cls)
    return a1 + a2

abc = Abc()
print(abc.add(3, 4))
print(Abc.add1(3, 4))
print(Abc.add2(3, 4))