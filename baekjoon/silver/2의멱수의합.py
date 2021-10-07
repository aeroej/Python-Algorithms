# n = int(input())

# dp = [0, 1, 2, 3]  # X, 1 경우의 수, 2 경우의 수, ...
# power = [1, 2]  # 2**0, 2**1, 2**2, 2**3, 2**4, ...

# def isPower(num):
#   if num == power[-1]*2:
#     power.append(num)

# for i in range(len(dp), n+1):
#   cnt = 0
#   for j in range(len(power)):
#     cnt += dp[i-power[j]]  # dp[n-1] + dp[n-2] + dp[n-4] + ...
#   isPower(n)
#   dp.append(cnt)  # dp.append(dp[n-1] + dp[n-2] + dp[n-4] + dp[n-8] + ...)

# print(dp)



n = int(input())
dp = [0, 1, 2]

for i in range(3, n+1):
  if i%2:  # 홀수
    dp.append(dp[i-1])
  else:  # 짝수
    dp.append(dp[i-1] + dp[i//2])

print(dp[n])
