from collections import deque
import sys


def dfs(graph, n1, visited):
    visited[n1] = True
    answer.append(n1)
    for i in range(m):
        if n1 in graph[i]:
            n2 = graph[i][0] if n1 == graph[i][1] else graph[i][1]
            if not visited[n2]:
                dfs(graph, n2, visited)


def bfs(graph, start, visited):
    queue = deque()
    queue.append(start)
    visited[start] = True
    while queue:
        n1 = queue.popleft()
        answer.append(n1)
        for i in range(m):
            if n1 in graph[i]:
                n2 = graph[i][0] if n1 == graph[i][1] else graph[i][1]
                if not visited[n2]:
                    queue.append(n2)
                    visited[n2] = True


n, m, v = map(int, input().split())
graph = []
for _ in range(m):
    n1, n2 = map(int, sys.stdin.readline().rstrip().split())
    graph.append(sorted([n1, n2]))
graph = sorted(graph, key=lambda x: (x[0], x[1]))

answer = []
visited = [False] * (n+1)
dfs(graph, v, visited)
print(' '.join(map(str, answer)))

answer = []
visited = [False] * (n+1)
bfs(graph, v, visited)
print(' '.join(map(str, answer)))
