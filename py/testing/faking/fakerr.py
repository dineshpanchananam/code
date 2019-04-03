from faker import Faker
f = Faker()
print(f.name())
print(f.address())
for i in range(10):
  print(f.name())
  print(f.address())
  print(f.text())
  print()