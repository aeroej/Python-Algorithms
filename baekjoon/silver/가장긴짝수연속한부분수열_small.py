import sys
sys.setrecursionlimit(10**6)


def dfs(v, length, k):  # 수열 s의 인덱스, 연속한 부분수열의 길이, 종료조건 k
  if k < 0:  # 홀수를 k+1번 삭제한 경우
    dp.append(length)
    return
  if v >= len(s):  # 모든 수열을 확인한 경우
    dp.append(length)
    return

  if s[v] == 0:  # 홀수
    dfs(v+1, length, k-1)
  else:  # 짝수
    dfs(v+1, length+1, k)


if __name__ == "__main__":
  n, k = map(int, sys.stdin.readline().split())
  s = list(map(lambda x: (int(x)+1) % 2, sys.stdin.readline().split()))  # 홀수는 0, 짝수는 1

  dp = []

  dfs(0, 0, k)
  for i in range(1, n-1):
    if s[i] == 0 and s[i+1] == 1:  # 홀수와 짝수가 인접한 경우
      dfs(i+1, 0, k)

  print(max(dp))
