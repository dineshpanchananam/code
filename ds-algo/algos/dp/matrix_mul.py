def pmat(matrix):
  for row in matrix:
    print row  

inf = float('inf')
mat = [[40, 20], [20, 30], [30, 10], [10, 30], [30, 40], [40, 10], [10, 1]]
n = len(mat)
dp = [[0] * n for i in xrange(n)]
pos = [[""] * n for i in xrange(n)]
breaks = [[-1] * n for i in xrange(n)]

for i in xrange(n):  
  pos[i][i] = chr(65 + i)

for i in xrange(1, n):
  for j in xrange(n-i):
    fst, lst = j, i + j
    ans = inf
    for k in range(fst, lst):
      value = dp[fst][k] + dp[k+1][lst] + mat[fst][0] * mat[k+1][0] * mat[lst][1]
      if value < ans:
        pos[fst][lst] = "(" + pos[fst][k] + pos[k+1][lst] + ")"
        breaks[fst][lst] = k
        ans = min(ans, value)
    dp[fst][lst] = ans
    
    
def form(l, r):
  if l == r:
    return pos[l][l]
  if l == r - 1:
    return "(" + pos[l][l] + pos[r][r] + ")"    
  m = breaks[l][r]
  left, right = [l, m], [m+1, r]
  return "(" + form(*left) + form(*right) + ")"

print dp[0][-1] 
print pos[0][-1][1:-1]
print form(0, n-1)[1:-1]