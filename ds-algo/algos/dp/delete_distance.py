class Solution(object):
  def minDistance(self, s1, s2):
    m, n = len(s1), len(s2)
    cache = [[0] * (n+1) for _ in xrange(m+1)]
    for i in xrange(m):
      cache[i+1][0] = i + 1
    for j in xrange(n):
      cache[0][j+1] = j + 1
      
    for i in xrange(1, m+1):
      for j in xrange(1, n+1):
        if s1[i-1] != s2[j-1]:
          cache[i][j] = min(cache[i-1][j] + 1 , cache[i][j-1] + 1)
        else:
          cache[i][j] = cache[i-1][j-1]
    
    return cache[m][n]

"""
   l e e t
d  
e
l
e
t
e
"""

s = Solution()
print s.minimumDeleteSum("delete", "leet")