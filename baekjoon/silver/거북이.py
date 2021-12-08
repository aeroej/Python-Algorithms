import sys
si = sys.stdin.readline


def tutle(moves):
  x = [0, 0]  # -x, +x
  y = [0, 0]  # -y, +y

  dx = -1
  dy = 0
  tt = [0, 0]

  for move in moves:
    if move == 'F':
      tt[0] += dx
      tt[1] += dy

    elif move == 'B':
      tt[0] -= dx
      tt[1] -= dy

    elif move == 'L':
      if dx == 0:  # y가 1 또는 -1인 경우
        dx, dy = -dy, 0
      else:
        dx, dy = 0, dx

    elif move == 'R':
      if dx == 0:
        dx, dy = dy, 0
      else:
        dx, dy = 0, -dx

    if tt[0] < x[0]:
        x[0] = tt[0]
    elif tt[0] > x[1]:
        x[1] = tt[0]
    if tt[1] < y[0]:
        y[0] = tt[1]
    elif tt[1] > y[1]:
        y[1] = tt[1]

  return x, y


t = int(si())
for _ in range(t):
  moves = si().rstrip()
  x, y = tutle(moves)
  print((x[1] - x[0]) * (y[1] - y[0]))
