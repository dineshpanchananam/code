from time import sleep

def search(arr, target, last=False):
  low, high, index = 0, len(arr) - 1, -1
  while low <= high:
    mid = (low + high) / 2
    if arr[mid] < target:
      low = mid + 1
    elif arr[mid] > target:
      high = mid - 1
    else:
      index = mid
      low, high = [mid + 1, high] if last else [low, mid - 1]
  return index
  
arr = [1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 4, 4, 5, 6, 7, 9]
arr = [2] * 10000
for target in range(1, 10):
  fst = search(arr, target)
  lst = search(arr, target, last=True)
  print target, (lst - fst + 1) if fst != -1 else 0