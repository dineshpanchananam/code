def lcs(a, b):
  m, n = len(a), len(b)
  dp = [[0] * (1+n) for i in xrange(m+1)]
  for i in xrange(1, m+1):
    for j in xrange(1, n+1):
      if a[i-1] == b[j-1]:
        dp[i][j] = 1 + dp[i-1][j-1]
      else:
        dp[i][j] = max(dp[i-1][j], dp[i][j-1])
  # tailing to get actual LCS
  x, y = m, n
  stack = []
  while x and y:
    if dp[x][y] == dp[x-1][y]:
      x, y = x-1, y
    elif dp[x][y] == dp[x][y-1]:
      x, y = x, y-1
    else:
      stack.append(a[x-1])
      x, y = x-1, y-1
  return dp[-1][-1], "".join(stack[::-1])
  
a = "abcgdef"
b = "dxabfhgexf"
print lcs(a, b)