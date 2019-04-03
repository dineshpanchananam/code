import random as r

r.seed(11)
n = 10
v = [r.randint(10, 200) for _ in xrange(n)]
w = [r.randint(1, 10) for _ in xrange(n)]
# print v
# print w
s = 36

cache = {}

def solve(wt, i, n, took):
  key = "({}, {})".format(wt, i)
  if n == i or wt == 0:
    return 0, took
  elif key not in cache:
    x, t1 = solve(wt, i + 1, n, took)
    if w[i] <= wt:
      y, t2 = solve(wt - w[i], i + 1, n, took)
      x, t1 = (y + v[i], t2 + [(w[i], v[i])]) if x < (y + v[i]) else (x, t1)
    cache[key] = (x, t1)
  return cache[key]
     
p, vals = solve(s, 0, len(w), [])
print p
print len(vals)
print len(cache)  
print "\n" * 2

memo = {}
def solve1(s, i):
  global v, w
  key = "[{}, {}]".format(s, i)
  if i < 0:
    return 0
  if key not in memo:
    memo[key] = solve1(s, i - 1)
    if w[i] <= s:
      memo[key] = max(memo[key], v[i] + solve1(s - w[i], i - 1))
  return memo[key]

x = solve1(s, len(w) - 1)

i, j = len(w)-1, s
form = "[{}, {}]"
ans = []
while j:
  if i > 0:
    k1 = form.format(j, i)
    k2 = form.format(j, i-1)
    if memo[k1] !=  memo[k2]:
      ans.append([w[i], v[i]])
      j -= w[i]
    i -= 1
  else:
    ans.append([w[i], v[i]])
    j -= w[i]
    
print x
# print ans, len(ans)
print len(memo)
print "\n" * 2



def botup(s):
  global v, w
  n = 2
  dp = [[0] * (1 + s) for _ in xrange(2)]
  exp = [[[] for x in xrange(1 + s)] for y in xrange(2)]
  for k in xrange(1, n):
    i = k & 1
    for j in xrange(1, s+1):
      dp[i][j] = dp[i-1][j]
      exp[i][j] = exp[i-1][j]
      if w[k-1] <= j:
        sub = dp[i-1][j-w[k-1]] + v[k-1]
        if dp[i][j] < sub:
          dp[i][j] = sub
          exp[i][j] = [(w[k-1], v[k-1])] + exp[i-1][j-w[i-1]]
      
  # row, col = len(w), s
  # wts, vls = [], []
  # ans = 0
  # while row:
  #   if dp[row][col] != dp[row-1][col]:
  #     ans += w[row-1]
  #     col -= w[row-1]
  #     # print [w[row-1], v[row-1]]
  #   row = row-1
  print sum(row[-1] for row in exp[n & 1][-1])
  print "*"
  return dp, exp[n & 1][-1]

dp, sol = botup(s)
print sol
print len(sol)
print dp[1][-1]
print len(dp) * len(dp[0])
print "\n" * 2

# greedy
wf = map(float, w)
vf = map(float, v)
df = [(x / y, y) for (x, y) in zip(vf, wf)]
df.sort(key=lambda x: -x[0])

rem, ans = s, 0
taken = 0
for (d, w1) in df:
  if rem > 0:
    can_take = w1 * min(1.0, rem / w1)
    rem -= can_take
    ans += d * can_take
    taken += 1
print sum(wf)
print ans
print s, rem
print taken

print "\n" * 2
rem, ans = s, 0
taken = 0
for (d, e) in zip(v, w):
  if rem >= e:
    rem -= e
    ans += d
    taken += 1
print ans
print "left", rem
print taken