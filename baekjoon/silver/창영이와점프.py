from collections import deque
import sys
def input(): return sys.stdin.readline().split()

n, k = map(int, input())
l = list(map(int, input()))

left = 0
dp = [0, 0]  # 점프 1번 사용한 경우, 가로막힌 경우

for right in range(n-1):
  if l[right] > k:  # 점프해야하는 경우
    blocks = right - left + 1
    dp[1] = max(dp[1], dp[0] + blocks)
    dp[0] = blocks
    left = right + 1

blocks = n-1 - left + 1
dp[1] = max(dp[1], dp[0] + blocks)

print(max(dp))
