#!/bin/python

import sys

def hackerlandRadioTransmitters(x, k):
  start = x[0]
  count, source = 0, x[0]
  x = sorted(set(x))
  last = 0
  sources = []
  print x
  for i in x:
    if source < i:    
    else:
      if source - i <= k:
        source
      
    if source and source < i:
      if i - source > k:
        start = i
    else:
      if i - start == k:
        source = i
        sources.append(i)
        count += 1
      elif i - start > k:
        source = last
        sources.append(source)
        count += 1
      last = i
  print sources
  return count
  
if __name__ == "__main__":
    result = hackerlandRadioTransmitters([7, 2, 4, 6, 5, 9, 12, 11], 2)
    print result