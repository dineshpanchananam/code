class Solution(object):  
  def longestPalindromeSubseq1(self, s):
    n = len(s)
    dp = [[0] * n for _ in xrange(n)]
    for i in xrange(n):
      dp[i][i] = 1
    for seg in xrange(2, n + 1):
      for start in xrange(n - seg + 1):
        end = start + seg - 1
        if s[start] == s[end]:
          if seg == 2:
            dp[start][end] = 2
          else:
            dp[start][end] = 2 + dp[start+1][end-1]
        else:
          dp[start][end] = max(dp[start+1][end], dp[start][end-1])
    return dp[0][-1]
  
  def longestPalindromeSubseq(self, s):
    if len(set(s)) == 1:
      return len(s)
    else:
      return self.longestPalindromeSubseq1(s)
      

class Solution1(object):  
  def longestPalindromeSubseq(self, s):
    n = len(s)
    dp = [[0] * n for _ in xrange(n)]
    def solve(x, y):
      if x > y:
        return 0
      elif dp[x][y]:
        return dp[x][y]
      elif x == y:
        dp[x][y] = 1
      elif s[x] == s[y]:
        dp[x][y] = 2 + solve(x + 1, y - 1)
      else:
        dp[x][y] = max(solve(x + 1, y), solve(x, y - 1))
      return dp[x][y]
    return solve(0, n-1)

x = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz"        
s = Solution1()
print s.longestPalindromeSubseq(x)