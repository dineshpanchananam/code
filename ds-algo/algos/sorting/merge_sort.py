def merge(a, b):
  i, j = 0, 0
  m, n = len(a), len(b)
  merged = []
  while i < m and j < n:
    if a[i] < b[j]:
      merged.append(a[i])
      i += 1
    else:
      merged.append(b[j])
      j += 1
  while i < m:
    merged.append(a[i])
    i += 1
  while j < n:
    merged.append(b[j])
    j += 1
  return merged

def merge_sort(a):
  if len(a) > 1:
    mid = len(a) / 2
    left, right = map(merge_sort, (a[:mid], a[mid:]))
    return merge(left, right)
  else:
    return a

if __name__ == '__main__':
  a = [3, 2, 1, 5, 4, 6, -9]
  print("before", a)
  result = merge_sort(a)
  print('after ', result)