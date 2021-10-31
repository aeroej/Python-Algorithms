# dfs 시간초과
# import sys

# def dfs(depth):
#   global cost
#   if depth >= n:
#     cost = min(cost, sum(stack))
#     return

#   for i in range(3):
#     if visited[depth-1] == color[i]:
#       continue
    
#     visited[depth] = color[i]
#     stack.append(graph[depth][i])
#     dfs(depth + 1)

#     visited[depth] = ''
#     stack.pop()


# if __name__ == "__main__":
#   n = int(input())
#   graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

#   visited = ['']*n
#   color = ['R', 'G', 'B']

#   stack = []
#   cost = 1e9

#   for i in range(3):
#     visited[0] = color[i]
#     stack.append(graph[0][i])
#     dfs(1)

#     visited[0] = ''
#     stack.pop()

#   print(cost)



import sys

n = int(input())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

for i in range(1, n):
  graph[i][0] = graph[i][0] + min(graph[i-1][1], graph[i-1][2])
  graph[i][1] = graph[i][1] + min(graph[i-1][0], graph[i-1][2])
  graph[i][2] = graph[i][2] + min(graph[i-1][0], graph[i-1][1])

print(min(graph[n-1]))