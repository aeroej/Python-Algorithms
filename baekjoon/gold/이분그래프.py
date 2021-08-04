import sys
sys.setrecursionlimit(10**6)

k = int(input())
for _ in range(k):
  v, e = map(int, sys.stdin.readline().rstrip().split())
  visited = [0]*(v+1)

  graph = []
  for _ in range(e):
    graph.append(list(map(int, sys.stdin.readline().rstrip().split())))

  visited[graph[0][0]] = 1
  visited[graph[0][1]] = -1

  flag = True
  for i in range(1, e):
    x = graph[i][0]
    y = graph[i][1]
    if visited[x] == 0 and visited[y] != 0:
      visited[x] = -visited[y]
    elif visited[x] != 0 and visited[y] == 0:
      visited[y] = -visited[x]
    elif visited[x] == visited[y] != 0:
      flag = False
      break
    elif visited[x] == visited[y] == 0:
      visited[x] = 1
      visited[y] = -1

  print("YES" if flag else "NO")



# BFS로 풀어라. 독립된 그래프가 포함된 경우, 임의로 1과 -1을 지정해준다는 것 자체가 틀렸다.