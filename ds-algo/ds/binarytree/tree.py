from time import sleep

class Tnode:
  def __init__(self, data, l=None, r=None):
    self.data = data
    self.left = l
    self.right = r
    
  def po(self):
    if self.left:
      self.left.po()
    if self.right:
      self.right.po()
    print self.data,
  
  def io(self):
    if self.left:
      self.left.io()
    print self.data,
    if self.right:
      self.right.io()

  def pro(self):
    print self.data,
    if self.left:
      self.left.pro()
    if self.right:
      self.right.pro()
  
  def po_it(self):
    stack = [self]
    values = []
    while stack:
      node = stack.pop()
      values.append(node.data)
      if node.left:
        stack.append(node.left)
      if node.right:
        stack.append(node.right)
    for i in values[-1::-1]:
      print i,
    print
  
  def io_it(self):
    root = self
    stack = []
    while root or stack:
      if root:
        stack.append(root)
        root = root.left
      else:
        root = stack.pop()
        print root.data,
        root = root.right
    print
    
  def pre_it(self):
    stack = [self]
    while stack:
      root = stack.pop()
      if root:
        stack.append(root.right)
        stack.append(root.left)
        print root.data,
    print
  
  def lvl(self):
    stack = [self]
    while stack:
      kids = []
      for s in stack:
        print s.data,
        kids.append(s.left)
        kids.append(s.right)
      stack = [kid for kid in kids if kid]
      print "|",
    print


  def ht(self):
    lh = self.left.ht() if self.left else 0
    rh = self.right.ht() if self.right else 0
    return 1 + max(lh, rh)

if __name__ == "__main__":
  t = Tnode
  r = t(89, t(1, None, t(5, t(6), t(6))), t(2, t(3, t(90, t(890, t(92, t(91)))))))
  r.pro()
  print
  r.pre_it()
  r.io()
  print
  r.io_it()
  r.po()
  print
  r.po_it()
  r.lvl()
  print r.ht()