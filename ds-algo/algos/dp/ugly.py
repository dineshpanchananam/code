ugly = [1]
two = three = five = 0
for i in xrange(1500000):
  cand = min(2 * ugly[two], 3 * ugly[three], 5 * ugly[five])
  two += 1 if cand == 2 * ugly[two] else 0
  three += 1 if cand == 3 * ugly[three] else 0
  five += 1 if cand == 5 * ugly[five] else 0
  ugly.append(cand)
print ugly[-1]