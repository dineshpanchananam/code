# Definition for a binary tree node.
class TreeNode(object):
  def __init__(self, x, l=None, r=None):
    self.val = x
    self.left = l
    self.right = r

def preorder(r):
  if r:
    print r.val,
    preorder(r.left)
    preorder(r.right)

def inorder(r):
  if r:
    inorder(r.left)
    print r.val,
    inorder(r.right)

def postorder(r):
  if r:
    postorder(r.left)
    postorder(r.right)
    print r.val,

class Solution(object):
  def preorderTraversal(self, root):
    stack = [root]
    while stack:
      node = stack.pop()
      if node:
        print node.val,
        if node.right:
          stack.append(node.right)
        if node.left:
          stack.append(node.left)
    print
    
  def inorderTraversal(self, root):
    stack = []
    while True:
      if root:
        stack.append(root)
        root = root.left
      else:
        if not stack:
          break
        root = stack.pop()
        print root.val,
        root = root.right
    print
    
s = Solution()
t = TreeNode
r = t(4, t(2, t(1), t(3)) , t(5, t(6), t(7)))
preorder(r)
print
inorder(r)
print
postorder(r)
print
s.inorderTraversal(r)
s.preorderTraversal(r)