class Student(object):
  
  __FFLAGS = {
    'a': 'b',
    'c': 'd'
  }
  
  def __init__(self, name):
    self.name = name
  
  @classmethod
  def go_to_school(cls):
    print type(cls), cls
    print 'going to school'

  @staticmethod
  def buy_lunch():
    print 'bought lunch'
    Student.__hidden()

  '''
  with cls is the only
  commented code here
  '''
  @classmethod
  def with_cls(cls):
    print cls.__FFLAGS
    cls.__hidden()
    
  @classmethod
  def keys(cls):
    return cls.__FFLAGS.keys()

  @staticmethod
  def keys1():
    return Student.__FFLAGS.keys()
    
  @staticmethod
  def __hidden():
    print 'valley of mystic rivers'
    
  @classmethod
  def get_hold(cls):
    print cls.__name__
    cls.__hidden()
    Student.__hidden()


if __name__ == '__main__':
  anna = Student("Anna")
  anna.go_to_school()
  anna.buy_lunch()
  Student.buy_lunch()
  Student.go_to_school()
  Student.with_cls()
  print anna.keys()
  print anna.keys1()
  print Student.keys()
  print Student.keys1()
  anna.get_hold()
  Student.get_hold()