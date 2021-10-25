import sys
from collections import deque

n, k = map(int, input().split())
wheel = deque(['?']*n)
flag = True

for _ in range(k):
  num, alpha = sys.stdin.readline().split()
  wheel.rotate(int(num))

  if wheel[0] == '?':
    if alpha in wheel:
      flag = False
      break
    wheel[0] = alpha

  else:
    if wheel[0] != alpha:
      flag = False
      break


print(''.join(wheel) if flag else '!')
