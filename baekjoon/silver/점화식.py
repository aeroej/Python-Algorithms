def recursion(n):
  if n == 0:
    return 1

  if dp[n] != 0:
    return dp[n]

  for i in range(n):
    dp[n] += recursion(i) * recursion(n-1-i)
  
  return dp[n]


if __name__ =="__main__":
  n = int(input())
  dp = [0]*(n+1)
  print(recursion(n))
