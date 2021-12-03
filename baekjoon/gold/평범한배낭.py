# 배낭 채우기 문제 (Knapsack Problem) 냅색 DP
# https://gsmesie692.tistory.com/113


import sys
def input(): return sys.stdin.readline().split()

n, k = map(int, input())
dp = [[0 for _ in range(k+1)] for _ in range(n+1)]

for i in range(1, n+1):  # 물품 idx
  w, v = map(int, input())

  for j in range(1, k+1):  # 배낭 무게
    if w > j:  # 보석이 배낭보다 무거운 경우
      dp[i][j] = dp[i-1][j]
    else:  # 보석을 배낭에 담을 수 있는 경우
      dp[i][j] = max(dp[i-1][j], v + dp[i-1][j-w])

print(dp[n][k])
