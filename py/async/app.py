import asyncio
import time

async def blocking(n):
  primes = 2
  for i in range(5, n):
    for j in range(2, i):
      if i % j == 0:
         break
    else:
      primes += 1
  print(primes)
  asyncio.sleep(1)
  return primes

async def main():
  await asyncio.wait([
    blocking(8000),
    blocking(4000), 
    blocking(20)
  ])

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()
