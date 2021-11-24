import sys
def input(): return sys.stdin.readline()

n = int(input())
dp = [0] + list(map(int, input().split()))

for i in range(2, n+1):
  for j in range(1, int(i/2) + 1):
    if dp[i] < dp[i - j] + dp[j]:
        dp[i] = dp[i - j] + dp[j]

print(dp[-1])
