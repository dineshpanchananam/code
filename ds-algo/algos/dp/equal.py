#!/bin/python

import sys

def equal(arr):
  nops = lambda x : x / 5 + (x % 5) / 2 + (x % 5) % 2
  ans, minm = float('inf'), min(arr)
  for diff in xrange(5):
    ans = min(ans, sum(nops(i - minm + diff) for i in arr))
  return ans

def equal1(arr):
  inf = float('inf')
  minm, maxm = min(arr), max(arr)
  target = maxm-minm
  dp = [0] + [inf] * target
  for i in xrange(1, target+1):
    for jump in [1, 2, 5]:
      if i >= jump:
        dp[i] = min(dp[i], 1 + dp[i-jump])
  return sum(dp[x - minm] for x in arr)
  
if __name__ == "__main__":
    t = int(raw_input().strip())
    for a0 in xrange(t):
        n = int(raw_input().strip())
        arr = map(int, raw_input().strip().split(' '))
        result = equal(arr)
        print result