from tree import Tnode as t

class BST:
  def __init__(self):
    self.root = None
  
  def insert(self, val):
    new, root = t(val), self.root
    if root:
      while root:
        prev, left = root, root.data > val
        root = root.left if left else root.right
      if left:
        prev.left = new
      else:
        prev.right = new
    else:
      self.root = new
      
  def insert1(self, val):
    tmp = t(val)
    if not self.root:
      self.root = tmp
    else:
      pass



b = BST()
b.insert(8)
b.insert(0)
b.insert(1)
b.insert(7)
b.insert(6)
b.insert(5)
b.insert(4)
b.insert(3)
b.root.io()
print
b.root.po()
print
b.root.pro()
print 
print b.root.ht()
