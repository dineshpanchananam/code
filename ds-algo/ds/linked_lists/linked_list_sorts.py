from random import randint

'''
Linked List
Operations
pushLast
pushFront
popFront
popLast
remove(value)
removeAll(value)
removeWithFunction() - remove all values satisfying a function
size / length - done
contains - linear search - done
valueAt - ith value
addAllLast()
addAllFront() 
clear - done 

iterable - done

Functional Programming basics

map - done
filter
reduce 

mem info - should I ?

Sorts
insertion sort - done
bubble sort - done
merge sort - done
quick sort - pending

'''

class Node:
  
  def __init__(self, payload):
    self.data = payload
    self.link = None

class List:

  def __init__(self, *values):
    self.head = Node(0)
    for value in values:
      self.pushFront(value)
      self.reverse()

  def loadSampleData(self):
    self.clear()
    values = [randint(1, 100) for _ in range(20)]
    for value in values:
      self.pushFront(value)
    self.reverse()
  
  # O(N)
  def traverse(self):
    print str(self)

  # Time Complexity: O(N * N)
  # Space Complexity: O(1)
  def bubbleSort(self):
    changed = self.head.link != None
    while changed:
      current = self.head.link
      adjacent = current.link
      changed = False
      while None not in (current, adjacent):
        if current.data > adjacent.data:
          current.data, adjacent.data = adjacent.data, current.data
          changed = True
        current = current.link
        adjacent = adjacent.link

  def toArray(self):
    current = self.head.link
    populate = []
    while current != None:
      populate.append(current.data)
      current = current.link
    return populate
    
  def insertionSort(self):
    insertion_ptr = self.head.link
    if insertion_ptr:
      while insertion_ptr.link:
        start_ptr = insertion_ptr.link
        while start_ptr:
          if insertion_ptr.data > start_ptr.data:
            insertion_ptr.data, start_ptr.data = \
            start_ptr.data, insertion_ptr.data
          start_ptr = start_ptr.link
        insertion_ptr = insertion_ptr.link
      
  def quickSort(self):
    raise NotImplementedError("not implemented!")
    
  def pushFront(self, data):
    newData = Node(data)
    newData.link = self.head.link
    self.head.link = newData
    self.head.data += 1
    
  def reverse(self):
    current = self.head.link
    if current:
      adjacent = current.link
      while adjacent != None:
        adjacent_link = adjacent.link
        adjacent.link = current
        current, adjacent = adjacent, adjacent_link
      self.head.link.link = None
      self.head.link = current

  @staticmethod
  def asArray(one, *rest):
    ans = List()
    ans.pushFront(one)
    [ans.pushFront(_) for _ in rest]
    ans.reverse()
    return ans
    
  @staticmethod
  def mergeLists(a, b):
    aPtr = a.head.link
    bPtr = b.head.link
    ans = List()
    
    while aPtr != None and bPtr != None:
      if aPtr.data < bPtr.data:
        ans.pushFront(aPtr.data)
        aPtr = aPtr.link
      else:
        ans.pushFront(bPtr.data)
        bPtr = bPtr.link
        
    while aPtr != None:
      ans.pushFront(aPtr.data)
      aPtr = aPtr.link
      
    while bPtr != None:
      ans.pushFront(bPtr.data)
      bPtr = bPtr.link
    
    ans.reverse()
    return ans
    
  def append(self, payload):
    newData = Node(payload)
    current = self.head.link
    self.head.data += 1
    if current:
      while current.link:
        current = current.link
      current.link = newData
    
  def merge(self, newList):
    current = self.head.link
    self.head.data += newList.head.data
    while current.link:
      current = current.link
    current_2 = newList.head.link
    while current_2:
      current.link = Node(current_2.data)
      current = current.link
      current_2 = current_2.link
      

  def __merge(self, fst, flength, snd, slength):
    ans = Node(-1)
    current = ans
    i, j = flength, slength
    next_fst, next_snd = fst, snd
    while i != 0 and j != 0:
      if fst.data < snd.data:
        current.link = fst
        next_fst = fst.link
        current = current.link
        fst = next_fst
        i -= 1
      else:
        next_snd = snd.link
        current.link = snd
        current = current.link
        snd = next_snd
        j -= 1
    
    while i:
      current.link = next_fst
      next_fst = next_fst.link
      current = current.link
      current.link = None
      i -= 1
      
    while j:
      current.link = next_snd
      next_snd = next_snd.link
      current = current.link
      current.link = None
      j -= 1
    
    return ans.link
    
  def __splitHalf(self, headPtr, n):
    current = headPtr
    for _ in range(n/2):
      current = current.link
    return current
      
    
  def __mergeSort(self, headPtr, n):
    midPtr, half = self.__splitHalf(headPtr, n), n/2
    aPtr, bPtr = headPtr, midPtr
    if half > 1:
      aPtr = self.__mergeSort(headPtr, half)
    if n - half > 1:
      bPtr = self.__mergeSort(midPtr, n - half)
    return self.__merge(aPtr, half , bPtr, n - half)
    
  def mergeSort(self):
    headPtr = self.head.link
    n = self.head.data
    # not applicable for one or less nodes
    if n > 1:
      self.head.link = self.__mergeSort(headPtr, n)
  
  def quick_sort(self):
    if self.head.data:
      pivot = self.head.link.data
      print pivot
  
  def push(self, data):
    self.head.data += 1
    newNode = Node(data)
    newNode.link = self.head.link
    self.head.link = newNode
    return self
    
  def __str__(self):
    ans = []
    current = self.head.link
    while current:
      ans.append(str(current.data))
      current = current.link
    return "[{}]".format(", ".join(ans))
    
  def map(self, func):
    current = self.head.link
    ans = List()
    stitch = ans.head
    while current:
      stitch.link = Node(func(current.data))
      stitch = stitch.link
      current = current.link
    return ans
  
  def mapped(self, func):
    current = self.head.link
    while current:
      current.data = func(current.data)
      current = current.link
    return self
    
  def filtered(self, fn):
    tmp = self.head
    current = self.head.link
    while current:
      if not fn(current.data):
        node = current
        current = current.link
        tmp.link = current
        self.__delNode(node)
      else:
        tmp = tmp.link
        current = current.link
    return self
    
  def size(self):
    return self.head.data
    
  def __len__(self):
    return self.head.data
    
  def isEmpty(self):
    return self.head.data == 0
  
  def clear(self):
    if self.head.data:
      current = self.head.link
      while current.link:
        tmp = current
        current = current.link
        del tmp
      del current
    
  def contains(self, data):
    current = self.head.link
    found = False
    while current:
      if data == current.data:
        found = True
        break
      current = current.link
    return found
    
  def __delNode(self, ref):
    self.head.data -= 1
    del ref
    
  def __iter__(self):
    current = self.head.link
    while current:
      yield current.data
      current = current.link

x = List()
x.loadSampleData()
x.traverse()
x.bubbleSort()
x.traverse()
# x.insertionSort()
x.mergeSort()
assert x.toArray() == sorted(x.toArray())
List.asArray(1, 2, 4, 3).traverse

List.mergeLists(
  List.asArray(1, 3, 5), 
  List.asArray(2, 4, 6)).traverse()

x = List.asArray(4, 1, 3, 2, 6, 7, 5)
x.traverse()
x.append(4)
x.traverse()
x.merge(List.asArray(1, 2, 3, 4, 8))
# x.insertionSort()
x = List.asArray(2, 1, 4, 3, 7, 5, -89)
x.traverse()
x.quick_sort()
print x.map(lambda y: y * y)
print x.mapped(lambda y: y * y).filtered(lambda z: z % 2 != 0) 
x.traverse()
print [_ for _ in x]