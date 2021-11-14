import sys
def input(): return sys.stdin.readline().split()

n, m = map(int, input())
board = [list(map(int, input())) for _ in range(n)]

# 19개의 테트로미노
tetrominos = [
  [(0, 0), (0, 1), (0, 2), (0, 3)],  # 직선
  [(0, 0), (1, 0), (2, 0), (3, 0)],
  [(0, 0), (0, 1), (1, 0), (1, 1)],  # 박스
  [(2, 0), (2, 1), (1, 1), (0, 1)],  # 세로기역
  [(0, 0), (1, 0), (2, 0), (2, 1)],
  [(0, 0), (2, 1), (1, 1), (0, 1)],
  [(0, 0), (1, 0), (2, 0), (0, 1)],
  [(0, 0), (1, 0), (1, 1), (1, 2)],  # 가로기역
  [(0, 2), (1, 0), (1, 1), (1, 2)],
  [(0, 0), (0, 1), (0, 2), (1, 0)],
  [(0, 0), (0, 1), (0, 2), (1, 2)],
  [(0, 1), (1, 0), (1, 1), (1, 2)],  # ㅗ
  [(0, 0), (0, 1), (0, 2), (1, 1)],  # ㅜ
  [(1, 0), (2, 1), (1, 1), (0, 1)],  # ㅓ
  [(0, 0), (1, 0), (2, 0), (1, 1)],  # ㅏ
  [(0, 0), (1, 0), (1, 1), (2, 1)],  # 번개
  [(0, 1), (1, 1), (1, 0), (2, 0)],
  [(0, 0), (0, 1), (1, 1), (1, 2)],
  [(1, 0), (1, 1), (0, 1), (0, 2)]
]


def cal_tetromino(tetromino):
  num = 0

  for dx, dy in tetromino:
    nx, ny = x + dx, y + dy
    if (0 <= nx < n) and (0 <= ny < m):
      num += board[nx][ny]
    else:
      return 0

  return num


res = 0
for x in range(n):
  for y in range(m):
    for tetromino in tetrominos:
      res = max(res, cal_tetromino(tetromino))
        
print(res)


