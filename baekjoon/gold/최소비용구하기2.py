import sys
import heapq
from collections import deque
def input(): return sys.stdin.readline()

def dijkstra(start):
  h = []
  heapq.heappush(h, (0, start))  # 비용, 출발도시
  table[start] = 0

  while h:
    cost, x = heapq.heappop(h)  # 현재비용, 출발도시
    if cost > table[x]:  # 최단경로를 이미 계산한 경우 = 방문한 적 있는 경우
      continue
    for y, w in graph[x]:
      cost_y = cost + w
      if cost_y < table[y]:
        table[y] = cost_y
        pre[y] = x
        heapq.heappush(h, (cost_y, y))


def find(node):
  if pre[node] == 0:
    return
  else:
    track.appendleft(pre[node])
    find(pre[node])

    
n = int(input())
m = int(input())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
  s, e, w = map(int, input().split())
  graph[s].append((e, w))

INF = 1_000 * 100_000
table = [INF] * (n + 1)
pre = [0] * (n + 1)

start, end = map(int, input().split())
dijkstra(start)
print(table[end])

track = deque([end])
find(end)

print(len(track))
print(*track)
