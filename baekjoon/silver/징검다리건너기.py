import sys


def dfs(v, flag):
  global k
  if v >= n:  # 종료조건
    res.append(dp[v-1])
    return

  dp[v] = min(dp[v-1] + energy[v-1][0], dp[v-2] + energy[v-2][1])  # min(한 칸 점프, 두 칸 점프)

  if flag == True:
    dfs(v+1, True)

  else:
    jumpBig = dp[v-3] + k

    if jumpBig < dp[v]:  # 아주 큰 점프가 에너지를 더 아낄 경우
      dfs(v+1, False)
      dp[v] = jumpBig
      dfs(v+1, True)
    else:
      dfs(v+1, False)


if __name__ == "__main__":
  n = int(sys.stdin.readline())
  if n == 1:
    print(0); sys.exit(0)

  energy = [list(map(int, sys.stdin.readline().split())) for _ in range(n-1)]
  k = int(sys.stdin.readline())

  dp = [0]*n
  dp[1] = energy[0][0]  # 한 칸 점프
  if n == 2:
    print(dp[1]); sys.exit(0)

  dp[2] = min(energy[0][1], dp[1] + energy[1][0])  # min(한 칸 점프, 두 칸 점프)

  res = []
  dfs(3, False)  # vertex, 세 칸 점프 k 사용여부
  print(min(res))
