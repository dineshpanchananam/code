def insertion_sort(a):
  total_moves = 0
  for i in xrange(1, len(a)):
    index = i
    while index and a[index-1] > a[index]:
      a[index-1], a[index] = a[index], a[index-1]
      index -= 1
      total_moves += 1
  return total_moves

if __name__ == '__main__':
  a = [3, 2, 1, 5, 4, 6, -9]
  print("before", a)
  print("moves", insertion_sort(a))
  print('after ', a)