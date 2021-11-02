# import sys

# n = int(input())
# s = list(map(int, sys.stdin.readline().rstrip().split()))
# dp = [0]*n

# dp[0], maxNum = s[0], s[0]

# for i in range(1, n):
#   dp[i] = max(s[i], s[i] + dp[i-1])
#   maxNum = max(maxNum, dp[i])

# print(maxNum)



import sys

n = int(input())
s = list(map(int, sys.stdin.readline().rstrip().split()))

for i in range(1, n):
  s[i] = max(s[i], s[i] + s[i-1])

print(max(s))
