class lst:
  def __init__(this, data, link=None):
    this.data = data
    this.link = link
    
  def __getitem__(this, slic):
    stp = slic.step if slic.step else 1
    beg = slic.start if slic.start else 0
    end = slic.stop if slic.stop else 2 ** 63
    ans = []
    curr = this
    for i in xrange(beg):
      if curr:
        curr = curr.link
    while beg < end and curr:
      ans.append(curr.data)
      for i in xrange(stp):
        if curr:
          curr = curr.link
      beg += stp
    return ans
  
  def prepend(self, x):
    self.link = lst(self.data, self.link)
    self.data = x

  def append(self, x):
    curr = self
    while curr.link:
      curr = curr.link
    curr.link = lst(x)
  
L = lst
d = L(2, L(1, L(4, L(3))))
d.prepend(6)
d.prepend(7)
d.append(4)
d.append(10)
print d[2:4]
print d[:]
print d[:3]
print d[::]
print d[2:]

# l = iter(d)
# while l:
#   print l.next()
