import sys
si = sys.stdin.readline

dx = [2, 2, -2, -2, -1, 1, -1, 1]
dy = [-1, 1, -1, 1, 2, 2, -2, -2]

y, x = map(str, si().rstrip())
x = int(x)
y = ord(y) - ord('a') + 1

cnt = 0
for i in range(8):
  nx, ny = x + dx[i], y + dy[i]
  if (0 < nx <= 8) and (0 < ny <= 8):
    cnt += 1

print(cnt)
