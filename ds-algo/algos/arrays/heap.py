#    buildHeap
#    comparator

from copy import copy

class MaxHeap:
  def __init__(self, array=[], comparator=None):
    self.data = copy(array)
    self.n = len(self.data)
    self.comparator = comparator if comparator else lambda x, y : x < y
    self.buildHeap()
  
  def heapify(self):
    print "heapifying at ", self.data[self.size() - 1]
    self.maxHeapify(self.size() - 1)
  
  def heapifyx(self):
    lastIndex = self.size() - 1
    parent = lastIndex / 2
    while lastIndex != 0:
      if self.data[lastIndex] > self.data[parent]:
        self.data[lastIndex], self.data[parent] =  \
          self.data[parent], self.data[lastIndex]
        lastIndex = parent
        parent = lastIndex / 2
      else:
        break

  def maxHeapify(self, index):
    if index != 0:
      parent = (index - 1) / 2
      if self.data[parent] < self.data[index]:
        self.data[parent], self.data[index] = self.data[index], self.data[parent]
        self.maxHeapify(parent)
        
  def buildHeap(self):
    lastParent = self.size() / 2 - 1 # 0 indexing
    for i in range(lastParent, 0, -1):
      print i
  
  def extract(self):
    top = self.data[0]
    lastValue = self.data.pop()
    self.data[0] = lastValue
    self.heapify()
    return top
    
  def add(self, payload):
    self.data.append(payload)
    self.heapify()
  
  def isMaxHeap(self, startIndex=0):
    left = startIndex * 2 + 1
    right = left + 1
    hasLeft = True if left < self.size() else False
    hasRight = True if right < self.size() else False
    cond = (self.data[startIndex] >=  self.data[left]) if hasLeft else True
    cond = (self.data[startIndex] >= self.data[right]) if hasRight else cond
    if cond and hasLeft:
      cond = cond and self.isMaxHeap(left)
    if cond and hasRight:
      cond = cond and self.isMaxHeap(right)
    return cond

  def size(self):
    return len(self.data)
    
h = MaxHeap([8, 4, 5, 3, 1, 4, 11])
print h.isMaxHeap()
h.heapify()
print h.data
print h.isMaxHeap()
for i in [90, 900, 980]:
  h.add(i)
  print h.data, h.isMaxHeap()
  
print h.data
print h.isMaxHeap()
print MaxHeap([1, 2, 3]).isMaxHeap()