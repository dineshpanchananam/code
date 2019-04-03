from __future__ import print_function
import logging
import datetime as dt

def log(lvl):
  def with_logging(func):
    print("log " + lvl + " " + str(dt.datetime.now()))
    return func
  return with_logging
  

@log("INFO")
def yay():
  print("yay!")

@log("DEBUG")
def yag():
  pass
  
yay()
yag()