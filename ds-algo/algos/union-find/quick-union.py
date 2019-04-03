import random as r

n = 50000
links = []
roots = range(n)
for i in xrange(1, n-1):
  links.append([i-1, i+1])

r.shuffle(links)
  
def parent(x):
  while x != roots[x]:
    x = roots[x]
  return x

def find(x, y):
  return parent(x) == parent(y)
  
def union(x, y):
  roots[x] = roots[y]
  
for u, v in links:
  if not find(u, v):
    union(u, v)

count = set()
for i in xrange(n):
  count.add(parent(i))

def height(x):
  h = 1
  while x != roots[x]:
    x = roots[x]
    h += 1
  return h

print "components", len(count)
print "max height", sorted(map(height, range(n)))[-10:]