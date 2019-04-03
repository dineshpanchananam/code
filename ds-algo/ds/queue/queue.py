from random import randint
from time import time
import sys

class QueueInterface:
  
  def raise_exception(self):
    raise NotImplementedError
  
  def push(self, el):
    self.raise_exception()
  
  def pop(self):
    self.raise_exception()
  
  def front(self):
    self.raise_exception()
  
  def back(self):
    self.raise_exception()
  
  def size(self):
    self.raise_exception()
  
  def __len__(self):
    return self.size()
  
  def clear(self):
    self.raise_exception()
  
  def is_empty(self):
    return self.size() == 0

class Node:
  def __init__(self, payload):
    self.data = payload
    self.back_link = None
    self.front_link = None

class Queue(QueueInterface):
  def __init__(self):
    self.head = Node(0)
  
  def size(self):
    return self.head.data
  
  def front(self):
    if self.is_empty():
      raise IndexError("front of an empty queue")
    return self.head.front_link.data
  
  def back(self):
    if self.is_empty():
      raise IndexError("back of an empty queue")
    return self.head.back_link.data
  
  def push(self, el):
    node = Node(el)
    self.head.data += 1
    node.back_link = self.head
    back_node = self.head.back_link
    if back_node:
      back_node.back_link = node
      node.front_link = back_node
      self.head.back_link = node
    else:
      self.head.front_link = node
      node.front_link = self.head
      self.head.back_link = node
  
  def pop(self):
    if not self.is_empty():
      self.head.data -= 1
      front_node = self.head.front_link
      data = front_node.data
      if front_node.back_link == self.head:
        self.head.front_link = None
        self.head.back_link = None
      else:
        self.head.front_link = front_node.back_link
        self.head.front_link.front_link = self.head
        del front_node
      return data
    else:
      raise IndexError('pop from an empty queue')
  
  def clear(self):
    while not self.is_empty():
      self.pop()

def queue_tests(queue):
  assert queue.is_empty()

  queue.push(3)
  assert not queue.is_empty()
  assert queue.front() == 3
  assert queue.back() == 3
  assert len(queue) == 1

  queue.push(4)
  assert len(queue) == 2
  assert queue.front() == 3
  assert queue.back() == 4

  assert queue.pop() == 3
  assert len(queue) == 1
  assert queue.front() == 4
  assert queue.back() == 4
  assert queue.pop() == 4
  assert len(queue) == 0
  assert queue.is_empty()

  queue.push(5)
  assert queue.front() == 5
  assert queue.back() == 5
  assert len(queue) == 1

  queue.push(6)
  assert queue.front() == 5
  assert queue.back() == 6
  assert len(queue) == 2

  queue.clear()
  assert queue.is_empty()
  
def main():
  q = Queue()
  # queue_tests(q)
  n = 1000000
  
  t1 = time()
  for _ in range(n):
    q.push(_)
  assert len(q) == n
  assert q.front() == 0
  assert q.back() == n-1

  t2 = time()
  print "running with %d elements" % n
  print "took %0.2f seconds to push" % (t2 - t1)

  q.clear()
  
  t3 = time()
  print "took %0.2f seconds to pop" % (t3 - t2)
  print "took %0.2f seconds" % (t3 - t1)

if __name__ == "__main__":
  main()