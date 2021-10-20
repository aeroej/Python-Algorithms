import sys

n, m = map(int, input().split())
seq = sorted(map(int, sys.stdin.readline().split()))
stack = []
visited = [0]*n

def dfs(v, start):
  if v == m:
    print(*stack)
    return

  overlap = 0
  for i in range(start, n):
    if not visited[i] and overlap != seq[i]:
      visited[i] = 1
      stack.append(seq[i])
      overlap = seq[i]
      dfs(v+1, i)
      visited[i] = 0
      stack.pop()

dfs(0, 0)