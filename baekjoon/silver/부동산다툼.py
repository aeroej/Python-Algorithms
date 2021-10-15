import sys

n, q = map(int, input().split())
visited = [0]*(n+1)

for _ in range(q):
  x = int(sys.stdin.readline())
  stack = [x]

  while x > 1:
    x = x // 2
    stack.append(x)

  while stack:
    num = stack.pop()

    if visited[num] == 1:
      print(num)
      break
    elif len(stack) == 0:
      visited[num] = 1
      print(0)
