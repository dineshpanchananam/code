from __future__ import print_function
import zerorpc as z
import logging

class Any:
  def __init__(self):
    self.a, self.b = 0, 1
    self.ticket_id = 0
    
  def hello(self, name):
    return "hello, {}".format(name)

  @z.stream
  def fibs(self):
    while True:
      self.a, self.b = self.b, self.a + self.b
      yield str(self.a)

  @z.stream
  def gen_ticket(self):
    while True:
      self.ticket_id += 1
      yield self.ticket_id

s = z.Server(Any())
s.bind("tcp://0.0.0.0:4242")
s.run()
