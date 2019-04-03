def ts(i, j, a, k):
  pairs = []
  while i < j:
    x, y = a[i], a[j]
    if x + y == k:
      pairs.append([x, y])
      i, j = i + 1, j - 1
    elif x + y < k:
      i += 1
    else:
      j -= 1
  return pairs
  
s = [1, 3, 2, 5, 0, 4, 1, 0, 1]
s.sort()
print s
n, k = len(s), 6
i = 0
while i < n:
  while i + 1 < n - 2 and s[i] == s[i+1]:
    i += 1
  j, k = i + 1, n - 1
  while j + 1 < n - 1 and s[j] == s[j+1]:
    j += 1
  
  sub = ts(i+1, n-1, s, k - s[i])
  for x in sub:
    print [s[i]] + x
  i += 1
