import zerorpc as z

c = z.Client()
c.connect("tcp://0.0.0.0:4242")
print c.hello("Dinesh")
fibs = c.gen_ticket()
for i in range(10):
  print next(fibs)