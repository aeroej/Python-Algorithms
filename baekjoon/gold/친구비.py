import sys
def input(): return sys.stdin.readline().split()

def find(x):
  if p[x] < 0:  # x가 루트노드인 경우
    return x
  
  p[x] = find(p[x])
  return p[x]


# 비용이 적은 친구가 루트노드가 되는 것이 유리
def merge(x, y):
  x = find(x)
  y = find(y)

  if x == y:
    return

  if cost[x] < cost[y]:  # x의 친구비용이 더 저렴한 경우
    p[x] += p[y]  # y의 집합은 x의 집합으로 합류
    p[y] = x  # y의 루트노드는 x
  else:
    p[y] += p[x]
    p[x] = y


n, m, k = map(int, input())
cost = [0] + list(map(int, input()))  # idx 0 친구
p = [-1 for _ in range(n+1)]  # idx 0 친구

for _ in range(m):
  a, b = map(int, input())
  merge(a, b)

price = 0
for i in range(1, n+1):
  if p[i] < 0:
    price += cost[i]

if price <= k:
  print(price)
else:
  print("Oh no")
