import sys
from collections import deque
si = sys.stdin.readline


def ac():
  global seq
  flag = False

  for x in p:  
    if x == 'R':
      flag = not flag  # 비교연산자 !=  -->  flag != flag (X)

    elif x == 'D':
      if len(seq) == 0:
        print('error')
        return

      if flag:
        seq.pop()
      else:
        seq.popleft()

  if flag:
    seq.reverse()

  print('[' + ','.join(seq) + ']')
  return


t = int(si())
for _ in range(t):
  p = si().rstrip()
  n = int(si())
  seq = deque(list(si().rstrip()[1:-1].split(',')))

  if seq[0] == '':
    seq = []

  ac()
