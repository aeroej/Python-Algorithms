from collections import deque
import heapq


def solution(board):
    n = len(board[0])
    visited = [[-1]*n for _ in range(n)]
    visited[n-1][n-1] = 0
    print(dfs(n, board, visited, 0, 0, 0, 0))
    for _ in range(n):
      print(visited[_])
    return


def dfs(n, board, visited, x, y, px, py):
    if visited[x][y] > -1:
      return visited[x][y]
    else:
      visited[x][y] = 10e9

    q = []
    for dx, dy in (-1, 0), (1, 0), (0, -1), (0, 1):
        nx, ny = x + dx, y + dy
        if (0 <= nx < n) and (0 <= ny < n):
            if board[nx][ny] == 0:
                cost = dfs(n, board, visited, nx, ny, dx, dy) + 100
                if (px, py) != (dx, dy):
                    cost += 500
                visited[x][y] = min(visited[x][y], cost)


    return visited[x][y]


solution([[0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0], [
         0, 0, 0, 1, 0, 0, 0, 1], [0, 0, 1, 0, 0, 0, 1, 0], [0, 1, 0, 0, 0, 1, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0]])
# solution([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
# solution([[0, 0, 1, 0], [0, 0, 0, 0], [0, 1, 0, 1], [1, 0, 0, 0]])
