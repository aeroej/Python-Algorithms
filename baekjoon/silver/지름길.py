import heapq
import sys
def input(): return sys.stdin.readline().split()

n, d = map(int, input())
distance = [d] * (d+1)

graph = [[] for _ in range(d + 1)]
tmp = set([0, d])

for _ in range(n):
  a, b, c = map(int, input())
  if b <= d:  # 역주행 X
    graph[a].append((b, c))
    tmp.add(a)
    tmp.add(b)

tmp = sorted(tmp)
for i in range(len(tmp)-1):
  graph[tmp[i]].append((tmp[i+1], tmp[i+1] - tmp[i]))   # 인덱스: 출발노드, (도착노드, 비용)


def dijkstra():
  q = []
  heapq.heappush(q, (0, 0))  # (비용 0, 시작노드 0)
  distance[0] = 0  # 시작노드 0의 비용 0

  while q:
    dist, now = heapq.heappop(q)  # 현 거리, 현 노드
    if distance[now] < dist:  # 최단거리 테이블의 비용이 더 적을 때
      continue
    for i in graph[now]:  # (i[0]: 인접노드, i[1]: 현 노드에서 인접노드까지 비용)
      cost = dist + i[1]
      if cost < distance[i[0]]:
        distance[i[0]] = cost
        heapq.heappush(q, (cost, i[0]))

dijkstra()
print(distance[d])




# # 노드의 개수, 간선의 개수
# n, m = map(int, input().split())
# # 시작 노드 번호 (0)
# start = int(input())
# # 연결된 노드에 대한 정보를 담은 그래프
# graph = [[] for i in range(n+1)]
# # 무한으로 초기화한 최단 거리 테이블
# distance = [INF]*(n+1)

# # 그래프 초기화
# for _ in range(m):
#   a, b, c = map(int, input().split())
#   graph[a].append((b, c))  # a, b 노드와 비용 c


# def dijkstra(start):
#   q = []
#   heapq.heappush(q, (0, start))  # 시작노드에서 시작노드로 가는 최단거리는 0
#   distance[start] = 0  # 최단거리 테이블 초기화

#   while q:
#     dist, now = heapq.heappop(q)  # 최단거리 짧은 노드 꺼내기
#     if distance[now] < dist:  # 최단거리 테이블에 기록된 거리가 더 짧을 경우
#       continue
#     for i in graph[now]:  # 지금 노드와 인접한 노드정보
#       cost = dist + i[1]
#       if cost < distance[i[0]]:
#         distance[i[0]] = cost
#         heapq.heappush(q, (cost, i[0]))


# dijkstra(start)

# for i in range(1, n+1):
#   if distance[i] == INF:
#     print("INFINITY")
#   else:
#     print(distance[i])
