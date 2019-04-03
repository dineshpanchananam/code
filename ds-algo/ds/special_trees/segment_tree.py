class Tree:
  def __init__(self, data, l=None, r=None):
    self.left = l
    self.right = r
    self.data = data

def cons(a, b):
  rnge = b - a
  if rnge:
    end1 = a + rnge / 2
    l = cons(a, end1)
    r = cons(end1 + 1, b)
    return Tree([a, b], l, r)
  else:
    return Tree([a, b])  

def cons_i(a, b):
  leaves = [Tree([i, i]) for i in xrange(a, b+1)]
  while len(leaves) > 1:
    tmp, n = [], len(leaves)
    for i in xrange(n/2):
      lnode, rnode = leaves[i * 2], leaves[i * 2 + 1]
      tmp.append(Tree([lnode.data[0], rnode.data[1]], lnode, rnode))
    if n & 1:
      tmp.append(leaves[-1])
    leaves = tmp
  return leaves[-1]
        
def ino(r):
  if r:
    print r.data
    ino(r.left)
    ino(r.right)

def lvl(a, r):
  s = [r]
  count = 1
  while s:
    print [a[x.data[0]:x.data[1]+1] for x in s]
    s1 = []
    for x in s:
      if x.left:
        s1.append(x.left)
      if x.right:
        s1.append(x.right)
    s = s1
    count += len(s)
  return count
  

def build(seg, x):
  if x < len(seg) / 2:
    build(seg, 2 * x + 1)
    build(seg, 2 * x + 2)
    seg[x] = seg[2 * x + 1] + seg[2 * x + 2]

def b1(seg, a, x, i, j):
  if i == j:
    seg[x] = a[i]
  else:
    mid = (i + j) / 2
    l, r = 2 * x, 2 * x + 1
    b1(seg, a, l, i, mid)
    b1(seg, a, r, mid+1, j)
    seg[x] = seg[l] + seg[r]

a = [1, 2, 4, 3, 2, 1, 8, 7, 1]
a = range(1, 12, 2)
print a
n = len(a)
seg = [0] * (n-1) + a
build(seg, 0)
print seg
seg1 = [0] * (2 * n - 1)  
b1(seg1, a, 0, 0, n-1)
print seg1

tr = cons(0, len(a)-1)
tr1 = cons_i(0, len(a)-1)
lvl(a, tr)
print
print lvl(a, tr1)