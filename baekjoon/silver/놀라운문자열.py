import sys
from collections import defaultdict
si = sys.stdin.readline

def is_surprising():
  for i in range(1, len(x)):
    dicT = defaultdict(int)

    for j in range(0, len(x) - i):
      # x[j]와 x[j + i], j + i < len(x)
      y = x[j] + x[j + i]

      if dicT[y]:
        return False
      else:
        dicT[y] = 1
        
  return True


for _ in range(101):
  x = si().rstrip()
  if x == '*':
    break

  if is_surprising():
    print(x, "is surprising.")
  else:
    print(x, "is NOT surprising.")
  