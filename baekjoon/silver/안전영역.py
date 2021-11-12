import sys
sys.setrecursionlimit(10**6)
def input(): return sys.stdin.readline()


n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

# 건물 높이 : 1이상 100 이하의 정수
# 비는 1부터 100까지
# 영역의 개수 res의 초기값은 1(맑은 날씨), 최종값은 0(모두 잠겼을 때)


def dfs(x, y, rain):
  if (0 <= x < n) and (0 <= y < n):
    if graph[x][y] > rain and not visited[x][y]:
      visited[x][y] = 1
      dfs(x - 1, y, rain)
      dfs(x + 1, y, rain)
      dfs(x, y - 1, rain)
      dfs(x, y + 1, rain)

  return


res = 1

for rain in range(1, 101):
  visited = [[0]*n for _ in range(n)]
  cnt = 0

  for i in range(n):
    for j in range(n):
      if graph[i][j] > rain and not visited[i][j]:
        cnt += 1
        dfs(i, j, rain)

  if cnt == 0:
    break
  res = max(res, cnt)

print(res)
