from math import log
from binarytreenode import Node
import sys

class BinTree:
  
  
  def __init__(self):
    self.n = 0
    self.root = None
    
    
  def size(self):
    return self.n
    
    
  def insert(self, data):
    newNode = Node(data)
    self.n += 1
    if self.root:
      pos = self.n
      current = self.root
      ptr = int(log(self.n, 2)) - 1
      while ptr > 0:
        current = current.right if (1 << ptr) & pos else current.left
        ptr -= 1
      if pos & 1:
        current.right = newNode
      else:
        current.left = newNode
    else:
      self.root = newNode
      
  def preOrder(self):
    if self.root:
      self.root.preorder()
    print

  def inOrder(self):
    if self.root:
      self.root.inorder()
    print
    
  def iterPreOrder(self):
    if self.root:
      stack = [self.root]
      while stack:
        last = stack.pop()
        print last.data,
        if last.right:
          stack.append(last.right)
        if last.left:
          stack.append(last.left)
      print
      
  def iterPostOrder(self):
    if self.root:
      stack = [self.root]
      while stack:
        last = stack.pop()
        if last.right:
          stack.append(last.right)
        print last.data,
        if last.left:
          stack.append(last.left)
      print
        
  def postOrder(self):
    if self.root:
      self.root.postorder()
    print
  
  def contains(self, data):
    return False if (not self.root) else self.root.contains(data)
    
  def levelOrder(self):
    pass
  
  def rootToLeaf(self, data):
    return False if not self.root else self.root.rootToLeaf(data)

  def isBST(self):
    return False if self.root == None else self.root.isBST()

  def height(self):
    return 0 if self.root == None else self.root.length()

  def lvlOrder(self):
    if self.root:
      level = 0
      height = self.height()
      queue = [self.root]
      tmp = []
      print (2 ** (height - 1) - 1) * " ",
      while queue:
        el = queue[0]
        del queue[0]
        if level == height-1:
          sys.stdout.write(" {}".format(el.data))
        else:
          if queue:
            sys.stdout.write(" {} {}".format(el.data, (2 ** (height - level) - 3) * " "))
          else:
            sys.stdout.write(" {}".format(el.data))
        if el.left:
          tmp.append(el.left)
        if el.right:
          tmp.append(el.right)
        if not queue:
          level += 1
          queue, tmp = tmp, []
          sys.stdout.write("\n")
          if level < height:
            sys.stdout.write((2 ** (height - level - 1) - 1) * " ")


b = BinTree()

import itertools as it
cycle = it.cycle(range(10))

n = 2 ** 3 - 1

for i in range(n):
  b.insert(cycle.next())

# b.lvlOrder()
b.iterPreOrder()
b.preOrder()
b.postOrder()
b.iterPostOrder()