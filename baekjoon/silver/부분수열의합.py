import sys

def dfs(depth, stack):
  global res

  if depth >= n:
    if stack and sum(stack) == s:
      res += 1
    return

  stack.append(seq[depth])
  dfs(depth + 1, stack)
  stack.pop()
  dfs(depth + 1, stack)

if __name__ == "__main__":
  n, s = map(int, input().split())
  seq = list(map(int, sys.stdin.readline().split()))
  res = 0

  dfs(0, 0)
  print(res)
