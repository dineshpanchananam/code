import types

def abc():
  f = open("f.txt", 'w')
  print("called")
  yield f
  print("running after steps")
  f.close()
g = abc()
if isinstance(g, types.GeneratorType):
  print(next(g))
  g.close()

def inf(start=1):
  while True:
    yield start
    start += 1
  
series = inf(3)
count = 0
for i in series:
  count += 1
  if count <= 10:
    print(i)
  else:
    break