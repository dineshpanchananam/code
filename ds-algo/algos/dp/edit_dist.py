# d = [90, 9, 89, 98, 1, 0, 1]
# c = map(str, d)
# c.sort(cmp=lambda a, b : cmp(b+a, a+b))
# print "".join(sorted(map(str, d), cmp = lambda x, y: cmp(y + x, x + y)))
# print "".join(c)

def edit_dist(a, b):
  m, n = len(a), len(b)
  dp = [[0] * (n+1) for _ in xrange(m+1)]
  for i in xrange(n+1):
    dp[0][i] = i
  for i in xrange(1, m+1):
    dp[i][0] = i
  for i in xrange(1, m+1):
    for j in xrange(1, n+1):
      if a[i-1] == b[j-1]:
        dp[i][j] = dp[i-1][j-1]
      else:
        # a[i] != b[j]
        # delete a[i]
        delt = 1 + dp[i-1][j]
        # replace a[i] with b[j]
        rep = dp[i-1][j-1] + 1
        # insert b[j] at a[i]
        ins = 1 + dp[i][j-1]
        dp[i][j] = min(delt, rep, ins)          
  return dp[m][n]

print edit_dist("dinesh", "panchananam")
print edit_dist("panchananam", "dinesh")