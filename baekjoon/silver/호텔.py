import sys
def input(): return sys.stdin.readline().split()

c, n = map(int, input())
graph = [list(map(int, input())) for _ in range(n)]
dp = [1e15]*1101
dp[0] = 0

for i in range(1, 1101):
  for j in range(n):
    cost, people = graph[j]
    if people <= i:
      dp[i] = min(dp[i], dp[i - people] + cost)

print(min(dp[c:]))
