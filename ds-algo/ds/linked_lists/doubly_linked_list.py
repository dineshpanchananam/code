import sys

class Node(object):
  def __init__(self, data=None, next_node=None, prev_node = None):
    self.data = data
    self.next = next_node
    self.prev = prev_node


def tr(head):
  while head:
    sys.stdout.write("%s " % head.data)
    head = head.next
  print()

def SortedInsert(head, data):
  new_node = Node(data)
  if head == None:
    return new_node
  curr = head
  prev = head.prev
  while curr and curr.data < data:
    prev = curr
    curr = curr.next
  if not prev:
    new_node.next = head
    head.prev = new_node
    head = new_node
  else:
    if prev.next:
      new_node.next = prev.next
      new_node.next.prev = new_node
    prev.next = new_node
    new_node.prev = prev

  return head

def SortedInsertI(head, data):
  new_node = Node(data)
  if not head:
    return new_node
  curr = head
  while curr.next and curr.data < data:
    curr = curr.next

  if not curr.next:
    new_node.prev = curr
    curr.next = new_node
  else:
    if curr.prev:
      prev_node = curr.prev
      new_node.prev = prev_node
      new_node.next = prev_node.next
      if prev_node.next:
        prev_node.next.prev = new_node
      prev_node.next = new_node
    else:
      head.prev = new_node
      new_node.next = head
      head = new_node
      
  tr(head)
  return head

def Reverse(head):
  if head:
    curr = head
    prev = None
    while curr.next:
      tmp = curr
      prev = curr
      curr = curr.next
    
      
    head = curr    
  return head
  
  
    
head = None
head = SortedInsert(head, 1)
head = SortedInsert(head, 4)
head = SortedInsert(head, 2)
head = SortedInsert(head, 3)
head = SortedInsert(head, 7)
head = SortedInsert(head, 6)
head = SortedInsert(head, 9)
head = SortedInsert(head, 10)



"""
4
2 1 4 3
8
1 4 2 3 7 6 9 10
"""
p = lambda x: sys.stdout.write(str(x) + ' ')

for i in range(2):
  while head:
    p(head.data)
    last = head
    head = head.next
  print()
  while last:
    p(last.data)
    last = last.prev
  print()
  head = Reverse(head)
  