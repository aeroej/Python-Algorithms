import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split(' '))
visited = [0 for i in range(100001)]

def bfs(N, K, visited):
  queue = deque([N])
  while queue:
    v = queue.popleft()
    if v == K:
      return visited[K];
    for i in (v-1, v+1, v*2):
      if (-1<i<100001) and not visited[i]:
        queue.append(i)
        visited[i] = visited[v] + 1

print(bfs(N, K, visited))