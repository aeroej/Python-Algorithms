import sys
si = sys.stdin.readline

n = int(si())
road = list(map(int, si().split()))
city = list(map(int, si().split()))

before = 1_000_000_000
cost = 0

for i in range(n-1):
  if city[i] < before:
    before = city[i]

  cost += before * road[i]

print(cost)
