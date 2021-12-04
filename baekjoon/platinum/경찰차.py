# 참고한 사이트
# https://injae-kim.github.io/problem_solving/2020/03/11/baekjoon-2618.html
# https://ioqoo.tistory.com/41

# -------------


import sys
sys.setrecursionlimit(10 ** 6)
si = sys.stdin.readline


def dist(c1, c2):
  x1, y1 = cars[c1]
  x2, y2 = cars[c2]
  return abs(x1 - x2) + abs(y1 - y2)


def minPath(c1, c2): 
  if dp[c1][c2] > -1:
    return dp[c1][c2]
  
  case = max(c1, c2) + 1
  if case >= w + 2:  # IndexError : 경찰차 및 사건 좌표의 총 개수를 초과할 경우
    dp[c1][c2] = 0  # 방문
    return dp[c1][c2]

  '''
  minPath(c1, c2)
  dp[c1][c2] = min(minPath(case, c2) + dist(c1, case),  # i
               minPath(c1, case) + dist(c2, case))  # ii
  i) 경찰차1이 사건을 맡은 경우, 경찰차1의 좌표는 case가 된다. + 두 좌표 사이의 거리를 구한다.
  ii) 경찰차2가 사건을 맡은 경우, 경찰차2의 좌표는 case가 된다. + 두 좌표 사이의 거리를 구한다.
  '''
  path1 = minPath(case, c2) + dist(c1, case)  # 경찰차1이 사건을 맡은 경우
  path2 = minPath(c1, case) + dist(c2, case)  # 경찰차2가 사건을 맡은 경우

  if path1 < path2:
    path[c1][c2] = 1
    dp[c1][c2] = path1
  else:
    path[c1][c2] = 2
    dp[c1][c2] = path2

  return dp[c1][c2]


n = int(input())
w = int(input())

cars = [(1, 1), (n, n)]  # tuple 2 + w개 : 경찰차 및 사건 좌표
for _ in range(w):
  x, y = map(int, si().split())
  cars.append((x, y))

'''
dp[경찰차1의 좌표인덱스][경찰차2의 좌표인덱스] = 최소 거리
path[경찰차1의 좌표인덱스][경찰차2의 좌표인덱스] = 다음 사건을 맡은 경찰차 번호
'''
dp = [[-1] * (w + 2) for _ in range(w + 2)] 
path = [[-1] * (w + 2) for _ in range(w + 2)]   

minPath(0, 1)
print(dp[0][1])


c1, c2 = 0, 1
for _ in range(w):
  print(path[c1][c2])

  case = max(c1, c2) + 1 
  if case >= w + 2:  # IndexError : 경찰차 및 사건 좌표의 총 개수를 초과할 경우
    break

  if path[c1][c2] == 1:  # 경찰차1이 사건을 맡았음
    c1 = case
  else:  # 경찰차2가 사건을 맡았음
    c2 = case

