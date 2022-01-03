import sys
from collections import deque
si = sys.stdin.readline

n = int(si())
times = [list(map(int, si().split())) for _ in range(n)]
times.sort(key=lambda x: (x[1], x[0]))

before = 0
cnt = 0

for s, e in times:
  if before <= s:
    cnt += 1
    before = e

print(cnt)
