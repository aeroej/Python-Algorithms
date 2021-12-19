import sys
si = sys.stdin.readline

n = int(si())
coins = [500, 100, 50, 10]
cnt = 0

for coin in coins:
  cnt += int(n / coin)
  n = n % coin

print(cnt)
