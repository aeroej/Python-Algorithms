import sys

def differ_taste(stack):
  global differ_min
  taste_s, taste_b = 1, 0

  for s, b in stack:
    taste_s *= s
    taste_b += b

  differ_min = min(differ_min, abs(taste_s - taste_b))
  return


def dfs(depth, stack):  # 재료를 넣는 순서가 상관없는 경우 --> depth는 오름차순 --> depth에 따른 종료조건
  if depth >= n:
    if stack:
      differ_taste(stack)
    return

  stack.append(taste[depth])
  dfs(depth+1, stack)
  stack.pop()
  dfs(depth+1, stack)


if __name__ == "__main__":
  n = int(input())
  taste = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
  differ_min = 1_000_000_000

  dfs(0, [])
  print(differ_min)



# def differ_taste(stack):
#   global differ_min
#   taste_s, taste_b = 1, 0

#   for s, b in stack:
#     taste_s *= s
#     taste_b += b

#   differ_min = min(differ_min, abs(taste_s - taste_b))
#   return


# def dfs(stack):  # 재료를 넣는 순서를 구분하는 경우 --> for문 사용
#   if stack:
#     differ_taste(stack)

#   for i in range(n):
#     if not visited[i]:
#       visited[i] = 1
#       stack.append(taste[i])
#       dfs(stack)

#       visited[i] = 0
#       stack.pop()


# if __name__ == "__main__":
#   n = int(input())
#   taste = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
#   visited = [0]*10
#   differ_min = 1_000_000_000

#   dfs([])
#   print(differ_min)
