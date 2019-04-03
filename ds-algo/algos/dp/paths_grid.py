m, n = 40, 50

tabu = [[0] * (n + 1) for _ in [0] * (m + 1)]
memo = [[0] * (n + 1) for _ in [0] * (m + 1)]

tabu[1][1] = 1
for i in xrange(1, m+1):
  for j in xrange(1, n+1):
    tabu[i][j] += tabu[i-1][j] + tabu[i][j-1]
print tabu[-1][-1]

def solve(m, n):
  if not memo[m][n]:
    if 1 not in [m, n]:
      ways1 = solve(m-1, n)
      ways2 = solve(m, n-1)
      memo[m][n] = ways1 + ways2
    else:
      memo[m][n] = 1
  return memo[m][n]
    
print solve(m, n)