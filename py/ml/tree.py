def more_than_150(f1):
  def wrapper(n):
    return "yay" if f1(n) > 150 else "nay"
  return wrapper

def sq_summer(f):
  def sub_sq(g):
    return sum(x*x for x in f(g))
  return sub_sq

def sq_sum_gt_150(f):
  pass

@sq_summer
def even_nums(y):
  return [x for x in y if x % 2 == 0]

@sq_sum_gt_150
def odd_nums(y):
  return [x for x in y if x % 2 == 1]

xs = range(10)
print even_nums(xs)
print odd_nums(xs)