from time import time

def parity_slow(p):
  bits = 0
  while p:
    bits ^= p & 1
    p = p & (p - 1)
  return bits

parity_cache = [parity_slow(i) for i in xrange(2 ** 16)]

def parity_fast(p):
  sz = 16
  mask = 0xFFFF
  return parity_cache[p >> 3 * sz] ^ \
  parity_cache[p >> 2 * sz & mask] ^ \
  parity_cache[p >> 1 * sz & mask] ^ \
  parity_cache[p & mask]

def parity_fastest(p):
  p ^= p >> 32
  p ^= p >> 16
  return parity_cache[p & 0xFFFF]
  
n = 26
t_1 = time()
print len(filter(parity_slow, xrange(2 ** 12, 2 ** n)))
t0 = time()
print len(filter(parity_fast, xrange(2 ** 12, 2 ** n)))
t1 = time()
print len(filter(parity_fastest, xrange(2 ** 12, 2 ** n)))
t2 = time()
print "%2f" % (t0 - t_1)
print "%2f" % (t1 - t0)
print "%2f" % (t2 - t1)