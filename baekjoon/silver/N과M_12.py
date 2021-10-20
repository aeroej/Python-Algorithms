import sys

n, m = map(int, input().split())
seq = sorted(map(int, sys.stdin.readline().split()))
stack = []


def dfs(v, start):
  if v == m:
    print(*stack)
    return

  overlap = 0
  for i in range(start, n):
    if overlap != seq[i]:
      stack.append(seq[i])
      overlap = seq[i]
      dfs(v+1, i)
      stack.pop()


dfs(0, 0)
