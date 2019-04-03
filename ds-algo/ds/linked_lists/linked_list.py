class Node:
  def __init__(self, data, link=None):
    self.data = data
    self.link = link

def rev(curr):
  prev = None
  while curr:
    cnext = curr.link
    curr.link = prev
    prev = curr
    curr = cnext
  return prev

def pprint(curr):
  res = []
  while curr:
    res.append(curr.data)
    curr = curr.link
  print res
  
def create(*args):
  ll = Node(None)
  ptr = ll
  for arg in args:
    tmp = Node(arg)
    ptr.link = tmp
    ptr = tmp
  return ll.link

class LinkedList:
  def __init__(self):
    self.head = Node(0)
  
  def push(self, data):
    self.head.link = Node(data, self.head.link)
    self.head.data += 1
  
  def pop(self):
    if self.head.link:
      self.head.link = self.head.link.link
      self.head.data -= 1
  
  def dump(self):
    curr = self.head.link
    res = []
    while curr:
      res.append(curr.data)
      curr = curr.link
    print res
  
  def size(self):
    return self.head.data

  def get(self, key):
    curr = self.head
    while curr and curr.data != key:
      curr = curr.link
    return curr

# n1 = create(7, 1, 6, 6, 5)
# n2 = create(5, 9, 2)
# n3 = LinkedList()

# carry = 0
# while n1 or n2:
#   a = n1.data if n1 else 0
#   b = n2.data if n2 else 0
#   print [a, b]
#   if (a + b) or carry:
#     c = a + b + carry
#     add, carry = c % 10, c / 10
#     n3.push(add)

#   n1 = n1.link if n1 else None
#   n2 = n2.link if n2 else None
e = LinkedList()
for i in [4, 3, 1, 2, 5, 6, 7, 8, 7, 7, 9, 60, 56]:
  e.push(i)

t = 7

ls, eq, gt = None, None, None
curr = e.head.link
while curr:
  prev = curr
  curr = curr.link
  if t == prev.data:
    prev.link = eq
    eq = prev
  elif t > prev.data:
    prev.link = ls
    ls = prev
  else:
    prev.link = gt
    gt = prev

def last(h):
  while h.link:
    h = h.link
  return h

def concat(args):
  lasts = map(last, args[:-1])
  for i in xrange(len(args)-1):
    lasts[i].link = args[i+1]
  return args[0]
  
pprint(ls)
pprint(eq)
pprint(gt)
pprint(concat([ls, eq, gt]))
      
# g1, g2 = e.get(6), e.get(4)
# g2.link = g1
# r1, r2 = e.head, e.head.link
# while r1 and r2:
#   if r1 == r2:
#     print "ring"
#     break
#   else:
#     r1, r2 = r1.link, r2.link
#     r2 = r2.link if r2 else None
