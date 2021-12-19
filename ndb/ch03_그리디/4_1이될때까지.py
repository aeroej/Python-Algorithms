# 단순 
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


# 그리디 
import sys
n, k = map(int, si().split())
cnt = 0

while n > 1:
    if n % k == 0:
        n = int(n / k)
        cnt += 1
    else:
        cnt += (n % k) 
        n -= (n % k)

print(cnt if n else cnt - 1)


