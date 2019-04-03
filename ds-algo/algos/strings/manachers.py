# a = "abaxex"
# t = ["$"]
# for i in a:
#   t.append("#")
#   t.append(i)
# t.extend(["#", "$"])
# n = len(t)
# p = [0] * n
# center, right = 0, 0
# for i in xrange(1, n-1):
#   mirror = 2 * center - i
#   if right > i:
#     p[i] = min(p[mirror], right - i)
#   while t[i + (p[i] + 1)] == t[i - (p[i] + 1)]:
#     p[i] += 1
#   if p[i] + i > right:
#     center = i
#     right = i + p[i]

# print p
# print "".join(t)
class Solution(object):
  def longestPalindrome(self, a):
    if a:
      t = ["@"]
      for i in a:
        t.append("#")
        t.append(i)
      t.extend(["#", "$"])
      n = len(t)
      p = [0] * n
      center, right = 0, 0
      for i in xrange(1, n-1):
        mirror = 2 * center - i
        if right > i:
          p[i] = min(p[mirror], right - i)
        while t[i + (p[i] + 1)] == t[i - (p[i] + 1)]:
          p[i] += 1
        if p[i] + i > right:
          center = i
          right = i + p[i]
      m = max(p)
      i = p.index(m)
      ans = t[i-m:i+m+1]  
      return "".join(t[j] for j in xrange(i-m+1, i+m, 2))
    return ""