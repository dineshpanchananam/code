from time import sleep

x = [1, 1, 

def find(x, low, high):
  sleep(1)
  print low, highx
  if x[low] <= x[high] or (high - low == 1):
    return low if x[low] <= x[high] else high
  mid = (low + high) / 2
  if x[mid] < x[low]:
    return find(x, low, mid)
  elif x[mid] > x[high]:
    return find(x, mid, high)
  
index = find(x, 0, len(x) - 1)
print x[index]