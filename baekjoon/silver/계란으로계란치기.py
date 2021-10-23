import sys

def dfs(depth):
  global res
  if depth >= n:
    res = max(res, sum(egg))
    return

  if egg[depth] == 1:  # 손에 든 계란이 이미 깨진 경우
    dfs(depth + 1)
    return

  if depth == n-1:  # 손에 든 계란은 마지막 계란
    if sum(egg) == n-1:  # 다른 계란은 모두 깨진 경우
      dfs(depth + 1)
      return

  for i in range(n):
    if depth == i:
      continue
    if egg[i] == 1:  # 계란이 이미 깨진 경우
      continue

    strength[i] -= weight[depth]
    strength[depth] -= weight[i]
    
    if strength[i] <= 0:
      egg[i] = 1
    if strength[depth] <= 0:
      egg[depth] = 1

    dfs(depth + 1)

    strength[i] += weight[depth]
    strength[depth] += weight[i]
    egg[i] = 0
    egg[depth] = 0


if __name__ == "__main__":
  n = int(input())
  strength, weight = [], []

  for _ in range(n):
    s, w = map(int, sys.stdin.readline().split())
    strength.append(s)
    weight.append(w)

  egg = [0]*n  # 깨진 경우 1
  res = 0

  dfs(0)
  print(res)
