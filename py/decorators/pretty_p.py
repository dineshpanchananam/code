def pretty_print(y):
  def wrapper(f):
    def sep(x):
      return y+y.join(f(x)) +y
    return sep
  return wrapper

@pretty_print("$")
def func(x):
  x= list(x)
  for i in xrange(0, len(x), 2):
    x[i] = x[i].upper()
  return x
  #print "|" + "|".join(x) + "|"
  
print func("abcde")

#|A|b|C|d|E|

  