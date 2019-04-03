from functools import lru_cache
from time import sleep

g = {}

def method1(x):
	g[x] = g.get(x, 0) + 1
	sleep(0.1)
	print(f'called {x}')
	return x * x

@lru_cache(maxsize=40)
def cacher(x):
	return method1(x)

count = 0
from random import randint
for j in range(4):
	for i in range(10):
		cacher(randint(0, 10))
		count += 1