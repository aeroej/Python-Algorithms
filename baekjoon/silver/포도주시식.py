import sys

n = int(input())
seq = [int(sys.stdin.readline()) for _ in range(n)]
seq = [0]*(n+1)

dp = [0]*n
dp[0] = seq[0]

dp[1] = seq[0] + seq[1]

if n >= 2:
  dp[2] = max(seq[1] + seq[2], dp[0] + seq[2], dp[1])

if n >= 3:
  for i in range(3, n):
    dp[i] = max(dp[i-3] + seq[i-1] + seq[i], dp[i-2] + seq[i], dp[i-1])

print(dp[n-1])


# dp[n] = n번째 마시는 경우
# n-3  n-2  n-1  n
# ?   x    o   o
#      ?   x   o

#       = n번째 마시지 않는 경우 = dp[i-1]
# n-4  n-3  n-2  n-1  n
# max   x    o    o   x
#      max   x    o   x
#                max  x


