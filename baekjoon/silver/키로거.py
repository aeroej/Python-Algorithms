import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

t = int(input())
for _ in range(t):
  pw = input()
  left = deque([])
  right = deque([])

  for x in pw:
    if x == '<':
      if len(left):
        right.appendleft(left.pop())
    elif x == '>':
      if len(right):
        left.append(right.popleft())
    elif x == '-':
      if len(left):
        left.pop()
    else:
      left.append(x)

  print(''.join(left + right))