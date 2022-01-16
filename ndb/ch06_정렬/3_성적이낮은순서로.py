import sys
si = sys.stdin.readline

n = int(si())
seq = [list(si().rstrip().split()) for _ in range(n)]
seq.sort(key = lambda x: int(x[1]))

for name, score in seq:
  print(name, end=' ')
