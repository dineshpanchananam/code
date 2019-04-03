from dataclasses import dataclass

@dataclass
class Abc:
  a: str
  b: int
  c: bool

abc = Abc(1, 2, None)
print([abc.a,
       abc.b])
d = Abc(c=None, a=1, b='a')
e = Abc(b='a', a=1, c=None)
print(d)
print(abc)
print(e)
print(d is e)
print(d == e)
