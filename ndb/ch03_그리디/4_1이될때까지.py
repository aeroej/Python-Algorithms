import sys
si = sys.stdin.readline
LIMIT = 100_000

n, k = map(int, si().split())

for cnt in range(LIMIT):
  if n == 1:
    print(cnt)
    break

  if n % k == 0:
    n = int(n/k)

  else:
    n -= 1
