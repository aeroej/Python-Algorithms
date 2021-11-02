import sys
sys.setrecursionlimit(10**6)

def dfs(x, y):
  if x >= n or y >= n:
    return 0

  if dp[x][y] != -1:
    return dp[x][y]  # 메모이제이션

  if left[x] > right[y]:
    dp[x][y] = dfs(x, y+1) + right[y] # 오른쪽 버리기
  else:
    discard_left = dfs(x+1, y) 
    discard_both = dfs(x+1, y+1) 
    dp[x][y] = max(discard_left, discard_both)  # max(왼쪽 버리기, 둘 다 버리기)

  return dp[x][y]
  

if __name__ == "__main__":  
  n = int(input())
  left = list(map(int, sys.stdin.readline().rstrip().split()))
  right = list(map(int, sys.stdin.readline().rstrip().split()))

  dp = [[-1 for _ in range(n)] for _ in range(n)]  # dp[x][y]
  dfs(0, 0)
  print(dp[0][0])



