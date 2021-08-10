import sys

def dfs(x, y):
  global sum
  flag = False
  if (0<=x<n) and (0<=y<n):
    visit[x][y] = 1
    for i in range(n):
      nx = x + dx[i]
      ny = y + dy[i]
      if (0<=nx<n) and (0<=ny<n):
        if visit[nx][ny] == 0:
          if (l <= abs(graph[x][y] - graph[nx][ny]) <= r):
            group.append([nx, ny])
            sum += graph[nx][ny]
            flag = True
            dfs(nx, ny)
  return (group, sum, flag)


if __name__ == '__main__':
  n, l, r = map(int, input().split())
  graph = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
  result = 0

  dx = [-1, 1, 0, 0]
  dy = [0, 0, -1, 1]

  while True:
    visit = [[0 for _ in range(n)] for _ in range(n)]
    result += 1
    exit = True
    for i in range(n):
      for j in range(n):
        if visit[i][j] == 0:
          group = [[i, j]]
          sum = graph[i][j]
          group, sum, flag = dfs(i, j)
          if flag == True:
            exit = False
            for x, y in group:
              graph[x][y] = int(sum/len(group))
    if exit == True:
      print(result-1)
      break


# import sys

# def dfs(x, y):
#   global sum
#   flag = False
#   if (0<=x<n) and (0<=y<n):
#     visit[x][y] = 1
#     if (0<=x-1<n) and (0<=y<n):
#       if visit[x-1][y] == 0:
#         if l <= abs(graph[x][y] - graph[x-1][y]) <= r:
#           group.append([x-1, y])
#           sum += graph[x-1][y]
#           flag = True
#           dfs(x-1, y)
#     if (0<=x+1<n) and (0<=y<n):
#       if visit[x+1][y] == 0:
#         if l <= abs(graph[x][y] - graph[x+1][y]) <= r:
#           group.append([x+1, y])
#           sum += graph[x+1][y]
#           flag = True
#           dfs(x+1, y)
#     if (0<=x<n) and (0<=y-1<n):
#       if visit[x][y-1] == 0:
#         if l <= abs(graph[x][y] - graph[x][y-1]) <= r:
#           group.append([x, y-1])
#           sum += graph[x][y-1]
#           flag = True
#           dfs(x, y-1)
#     if (0<=x<n) and (0<=y+1<n):
#       if visit[x][y+1] == 0:
#         if l <= abs(graph[x][y] - graph[x][y+1]) <= r:
#           group.append([x, y+1])
#           sum += graph[x][y+1]
#           flag = True
#           dfs(x, y+1)
#   return (group, sum, flag)


# if __name__ == '__main__':
#   n, l, r = map(int, input().split())
#   graph = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
#   result = 0

#   while True:
#     visit = [[0 for _ in range(n)] for _ in range(n)]
#     result += 1
#     exit = True
#     for i in range(n):
#       for j in range(n):
#         if visit[i][j] == 0:
#           group = [[i, j]]
#           sum = graph[i][j]
#           group, sum, flag = dfs(i, j)
#           if flag == True:
#             exit = False
#             for x, y in group:
#               graph[x][y] = int(sum/len(group))
#     if exit == True:
#       print(result-1)
#       break
 