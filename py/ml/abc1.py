from functools import wraps

def wraps(f):
  def wrapper(g):
    
    

def pretty_print(sep):
  def actual(func):
    def wrapper(args):
      return sep + sep.join(func(args)) + sep
    return wrapper
  return actual

def capify(f):
  @wraps(f)
  def wrapper(string):
    chars = f(string)
    return [x.upper() for x in chars]
  return wrapper

@pretty_print("#")
@capify
def to_chars(x):
  return list(x)

if __name__ == "__main__":
  print(to_chars("abcde"))

@capify
def to_char_arr(x):
  """This functions converts string to [char]"""
  return list(x)

#|A|b|C|d|E|