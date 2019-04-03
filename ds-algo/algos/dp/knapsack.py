def dp_knap(weights, values, target):
  n = len(values)
  dp = [[0 for i in xrange(target+1)] for j in xrange(n+1)]
  for i in xrange(1, n+1):
    for j in xrange(1, target+1):
      dp[i][j] = dp[i-1][j] if weights[i-1] > j else \
          max(dp[i-1][j], dp[i-1][j-weights[i-1]] + values[i-1])
  return dp
  

def items(dp):
  x, y, bag = len(dp) - 1, len(dp[0]) - 1, []
  while x:
    if dp[x][y] == dp[x-1][y-weights[x-1]] + values[x-1]:
      bag.append([weights[x-1], values[x-1]])
      y -= weights[x-1]
    x -= 1
  for row in sorted(bag, key=lambda x:x[0]):
    print "weight", row[0], "value", row[1]
  print 'W', 'V', reduce(lambda x, y: (x[0] + y[0], x[1] + y[1]), bag)
  return bag

# greedy
def greedy_knap(weights, values, target):
  densities = [(float(v) / w, w) for (v, w) in zip(values, weights)]
  sortd = sorted(densities, key=lambda x: -x[0])
  left, value = target, 0
  for d, w in sortd:
    if left > 0.001:
      p = min(left, w)
      value += p * d
      left -= p
  return value
  
weights = [4, 2, 1, 3, 5, 7, 8, 9, 10, 1, 2, 3, 4, 27]
values =  [8, 7, 2, 3, 1, 5, 1, 1, 3, 12, 1, 2, 4, 100]
target = 26

print greedy_knap(weights, values, target)
dp = dp_knap(weights, values, target)
items(dp)