from __future__ import print_function
def fibs():
  a, b = yield
  while True:
    yield a
    a, b = b, a + b

f = fibs()
f.send(3)
next(f)
f.send([3, 5])
for i in range(10):
  print(next(f), end=" ")
  if i == 5:
    f.close()