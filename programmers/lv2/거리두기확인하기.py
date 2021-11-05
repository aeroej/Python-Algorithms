# 2021 카카오 채용연계형 인턴십

from collections import deque


def solution(places):
    res = []
    for place in places:
        visited = [[0]*5 for _ in range(5)]
        res.append(check(place, visited))
    return res


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def check(place, visited):
    for i in range(5):
        for j in range(5):
            if place[i][j] == 'P' and visited[i][j] == 0:
                visited[i][j] = 1
                if bfs(i, j, place, visited) == 0:
                    return 0
    return 1


def bfs(x, y, graph, visited):
    queue = deque([[x, y]])

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (0 <= nx < 5) and (0 <= ny < 5) and visited[nx][ny] == 0:
                if graph[nx][ny] == 'P':
                    return 0
                if graph[x][y] == 'P' and graph[nx][ny] == 'O':
                    visited[nx][ny] = 1
                    queue.append([nx, ny])
    return 1
