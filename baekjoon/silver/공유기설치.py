import sys


def router(mid):
  cnt = 1
  idx = 0

  for i in range(1, n):
    if seq[i] - seq[idx] >= mid:
      cnt += 1
      idx = i

  return cnt


if __name__ == "__main__":
  n, c = map(int, input().split())
  seq = sorted([int(sys.stdin.readline().rstrip()) for _ in range(n)])
  res = 0

  left = 1
  right = seq[-1] - seq[0]

  while left <= right:
    mid = int((left + right) / 2)

    if router(mid) >= c:
      res = max(res, mid)
      left = mid + 1

    else:
      right = mid - 1

  print(res)



