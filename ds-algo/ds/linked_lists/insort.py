def insertion_sort(head):
  if head:
    sub = insertion_sort(head.next)
    curr, prev = sub, None
    while curr and curr.data < head.data:
      prev = curr
      curr = curr.next
    if prev:
      prev.next = head
      head.next = curr
      return sub
    else:
      head.next = sub
      return head
  return head
  
def sorted_insert(c1, node):
  if not c1:
    return node
  elif node.data < c1.data:
    node.next = c1
    return node
  curr, prev = c1, None
  while curr and curr.data < node.data:
    prev = curr
    curr = curr.next    
  node.next = prev.next
  prev.next = node
  return c1
    
def insertion_sort1(head):
  c1 = None
  c2 = head
  while c2:
    c2_next = c2.next
    c2.next = None
    c1 = sorted_insert(c1, c2)
    c2 = c2_next
  return c1
  
class L:
  def __init__(self, d, n=None):
    self.next = n
    self.data = d

d = L(29, L(23, L(82, L(11, L(3)))))
f = insertion_sort1(d)
while f:
  print f.data,
  f = f.next
print