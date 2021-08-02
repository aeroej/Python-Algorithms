import sys
sys.setrecursionlimit(10**6)

def dfs(x, y):
  if (0<=x<n) and (0<=y<m):
    if graph[x][y] == 1:
      graph[x][y] = -1
      dfs(x-1, y)
      dfs(x+1, y)
      dfs(x, y+1)
      dfs(x, y-1)
      return True
  return False

if __name__ == "__main__":
  t = int(input())
  for _ in range(t):
    n, m, k = map(int, input().split())
    graph = [[0 for _ in range(m)] for _ in range(n)]

    for _ in range(k):
      x, y = map(int, sys.stdin.readline().rstrip().split())
      graph[x][y] = 1

    cnt = 0
    for i in range(n):
      for j in range(m):
        if dfs(i, j) == True:
          cnt += 1
    
    print(cnt)

