class Node:
  def __init__(self, data, left=None, right=None):
    self.data = data
    self.left = left
    self.right = right
    
  def contains(self, data):
    if self.data == data:
      return True
    else:
      foundInLeft = False
      foundInRight = False
      if self.left:
        foundInLeft = self.left.contains(data)
      if (not foundInLeft) and self.right:
        foundInRight = self.right.contains(data)
      return foundInLeft or foundInRight
  
  def inorder(self):
    if self.left:
      self.left.inorder()
    print self.data, 
    if self.right:
      self.right.inorder()
  
  def preorder(self):
    print self.data,
    if self.left:
      self.left.preorder()
    if self.right:
      self.right.preorder()
  
  def postorder(self):
    if self.left:
      self.left.postorder()
    if self.right:
      self.right.postorder()
    print self.data,
  
  def rootToLeaf(self, data):
    if self.left == None and self.right == None:
      return self.data == data
    else:
      if self.left:
        leftResult = self.left.rootToLeaf(data - self.data)
        if (not leftResult) and self.right:
          return self.right.rootToLeaf(data - self.data)
        return leftResult
        
  def isBST(self):
    hasLeft = self.left != None
    hasRight = self.right != None
    isLeftBst, isRightBst = (not hasLeft), (not hasRight)
    if hasLeft and self.data >= self.left.data:
      isLeftBst = self.left.isBST()
    if hasRight and isLeftBst and self.data < self.right.data:
      isRightBst = self.right.isBST()
    return isLeftBst and isRightBst
      
  def bstInsert(self, data):
    newNode = Node(data)
    current = self
    while current.left != None or current.right != None:
      current = current.left if self.data >= data else current.right
    if data > current.data:
      current.right = newNode
    else:
      current.left = newNode
      
  def length(self):
    heightOfLeft = 0 if self.left == None else self.left.length()
    heightOfRight = 0 if self.right == None else self.right.length()
    return 1 + max(heightOfLeft, heightOfRight)
    
    