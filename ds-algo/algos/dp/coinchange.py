class Solution(object):
  def __init__(self):
    self.cache = {0: 0}
    self.inf = 10 ** 100

  def coinChange(self, coins, k):
    if k in self.cache:
      return self.cache[k]
    ans = self.inf
    for c in coins:
      if c <= k:
        subs = self.coinChange(coins, k - c)
        if subs >= 0:
          ans = min(ans, 1 + subs)
    self.cache[k] = -1 if ans == self.inf else ans
    print self.cache
    return self.cache[k]
    

class Solution1(object):
  def coinChange(self, coins, amount):
    c, inf = len(coins), 10 ** 100
    dp = [0] + [inf] * amount    
    for i in xrange(1, amount+1):
      for coin in coins:
        if i >= coin:
          dp[i] = min(dp[i], 1 + dp[i-coin])
    return dp[-1]    
    
amount = 11
coins = [1, 2, 5]

s = Solution1()
print s.coinChange(coins, amount)