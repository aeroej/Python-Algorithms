import sys

t = int(sys.stdin.readline())
for _ in range(t):
  p = int(sys.stdin.readline())
  res_c = 0
  res_name = ''

  for _ in range(p):
    c, name = sys.stdin.readline().split()
    if int(c) > res_c:
      res_c, res_name = int(c), name

  print(res_name)
