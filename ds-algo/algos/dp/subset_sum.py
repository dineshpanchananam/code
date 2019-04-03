def solve(d, target):
  n = len(d)
  dp = [[1] + [0] * target for _ in xrange(n+1)]
  for i in xrange(1, n+1):
    for j in xrange(1, target+1):
      x = d[i-1]
      if x <= j:
        dp[i][j] = dp[i-1][j-x]
      dp[i][j] |= dp[i-1][j]
  return bool(dp[-1][-1])

d = [1, 7, 2, 1, 2, 4, 5, 6]
target = 19
print solve(d, target)