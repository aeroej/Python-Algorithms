import sys

n, times = map(int, input().split())
point = [0, 0]
direct = (1, 0)
t0 = 0

for _ in range(n):
  t1, s = sys.stdin.readline().split()
  t1 = int(t1)
  
  x, y = direct
  point[0] += x * (t1 - t0)
  point[1] += y * (t1 - t0)

  if x:
    if s == 'left':
      x, y = y, x
    else:
      x, y = y, -x
  elif y:
    if s == 'right':
      x, y = y, x
    else:
      x, y = -y, x
  direct = (x, y)
  t0 = t1

x, y = direct
point[0] += x * (times - t0)
point[1] += y * (times - t0)
print(*point)
