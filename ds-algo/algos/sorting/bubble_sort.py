def bubble_sort(a):
  swaps, swapped = 0, True
  while swapped:
    swapped = False
    for i in xrange(1, len(a)):
      if a[i-1] > a[i]:
        a[i-1], a[i] = a[i], a[i-1]
        swapped = True
        swaps += 1
  return swaps
  
if __name__ == "__main__":
  a = [3, 2, 1, 5, 4, 6, -9]
  print("before", a)
  print("swaps", bubble_sort(a))
  print("after ", a)