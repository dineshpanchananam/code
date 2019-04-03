def fib(n):
  a, b = 0, 1
  for i in range(n):
    a, b = b, b + a
  return a

def fib1():
  a, b = 0, 1
  while True:
    a, b = b, a + b
    yield a
    
def fib(n):
  if n < 2:
    return n
  return fib(n-1) + fib(n-2)
  
def fib(n, cache={0: 1, 1: 1}):
  if n not in cache:
    cache[n] = fib(n-1) + fib(n-2)
  return cache[n]