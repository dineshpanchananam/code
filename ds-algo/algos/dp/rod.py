n = 50
p = [2, 5, 7, 8]

dp = [[0] * (n+1) for i in xrange(len(p)+1)]

for c in xrange(1, len(p)+1):
  for i in xrange(1, n+1):
    if c <= i:
      dp[c][i] = max(dp[c-1][i], dp[c][i-c] + p[c-1])
    else:
      dp[c][i] = dp[c-1][i]

print dp[-1][-1]
  
cache = {}
def solve(k):
  if k in cache:
    return cache[k]
  ans = 0
  for c in xrange(1, len(p)+1):
    if c <= k:
      ans = max(ans, p[c-1] + solve(k-c))
  cache[k] = ans
  return ans

print solve(50)