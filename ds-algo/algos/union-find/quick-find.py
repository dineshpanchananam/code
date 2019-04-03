import random as r

n = 50000
links = []

roots = range(n)
for i in xrange(1, n):
  links.append([i-1, i])
# r.shuffle(links)

count = n
def find(x, y):
  return roots[x] == roots[y]
  
def union(x, y):
  global count
  px = roots[x]
  count -= int(roots[x] != roots[y])
  for i in xrange(len(roots)):
    if roots[i] == px:
      roots[i] = roots[y]

for u, v in links:
  if not find(u, v):
    union(u, v)

def height(x):
  h = 1
  while x != roots[x]:
    x = roots[x]
    h += 1
  return h

print "components", count