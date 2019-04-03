def combs_recursive(a):
  ans = []
  if a:
    sub = combs_recursive(a[1:])
    sub = [''] if not sub else sub
    for x in sub:
      ans.append(x)
      ans.append(a[0] + x)
  return ans

def combs_iterative(a):
  n, ans = len(a), []
  for i in xrange(1<< n):
    tmp = []
    for j in xrange(n):
      if i & (1 << j):
        tmp.append(a[j])
    ans.append("".join(tmp))
  return ans
  
def perms_recursive(a):
  ans = []
  if a:
    sub = perms_recursive(a[1:])
    sub = [''] if not sub else sub
    for x in sub:
      for i in xrange(1 + len(x)):        
        ans.append(x[:i] + a[0] + x[i:])      
  return ans

def perms_iterative(a):
  ans = []
  if a:
    ans, tmp = [a[0]], []
    for i in a[1:]:
      for k in ans:
        for j in xrange(len(k)+1):
          tmp.append(k[:j] + i + k[j:])
      ans, tmp = tmp, []        
  return ans

def npk(a, k, index=0):
  if k == 0:
    return ['']
  n = len(a)
  sub = npk(a, k-1, index+1)
  if n - index > k:
    sub.extend(npk(a, k, index+1))
  return [i[:j] + a[index] + i[j:]
          for i in sub for j in xrange(len(i)+1)]
    
def nck(a, k, index=0):
  if k == 0:
    return ['']
  n = len(a)
  take, ignore = nck(a, k-1, index+1), []
  if n - index > k:
    ignore = nck(a, k, index+1)
  return [a[index] + x for x in take] + ignore

# print combs_iterative("abc")
# print combs_recursive("abc")
# print perms_iterative("abc")
# print perms_recursive("abc")
# print nck("abc", 2)
# print npk("abc", 2)

i = 1
for x in perms_iterative("abcd"):
  print i, x
  i += 1
  