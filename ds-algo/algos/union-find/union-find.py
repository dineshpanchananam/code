def root(x):
  while x != uf[x]:
    x = uf[x]
  return x
  
def connected(x, y):
  return root(x) == root(y)

def union(x, y, uf):
  i = root(x)
  j = root(y)
  uf[i] = j
  
n = 5
edges = [[1, 2], [2, 3], [3, 4]]
uf = [i for i in xrange(n)] 

for u, v in edges:
  if not connected(u, v):
    union(u, v, uf)
    print uf

for u, v in edges:
  print connected(u, v)
  