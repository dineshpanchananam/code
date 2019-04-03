class TrieNode:
  def __init__(self, payload):
    self.data = payload
    self.right = None
    self.down = None
  
class Trie:
  def __init__(self):
    self.head = TrieNode(0)
  
  def push(self, word):
    parent = self.head
    ptr = parent.down
    index, length = 0, len(word)
    system = True
    while system and (index < length):
      char = word[index]
      if ptr:
        current = ptr
        found = False
        while current:
          if current.data == char:
            break
          current = current.right
        if current:
          parent = current
          ptr = parent.down
        else:
          node = TrieNode(char)
          node.right = parent.down
          parent.down = node
          parent = node
          ptr = parent.down
          
      else:
        value = TrieNode(char)
        parent.down = value
        parent = parent.down
        ptr = parent.down
      index += 1

  def contains(self, word):
    index, length = 0, len(word)
    found = True
    ptr = self.head
    while (index < length) and found:
      char = word[index]
      current = ptr.down
      while current:
        if current.data == char:
          break
        current = current.right
      if current:
        ptr = current
      else:
        found = False
      index += 1
      
    return found
  

import random
import string
import time

n = 100000
array = []
trie = Trie()
insert_strings = [''.join([random.choice(string.ascii_lowercase) for _ in range(random.randint(3, 40))]) for _ in range(n)]

[trie.push(s) for s in insert_strings]
t2 = time.time()
count = 0
for s in insert_strings:
  if trie.contains(s):
    count += 1
t3 = time.time()

print t3 - t2, count
