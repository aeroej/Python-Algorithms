import sys

n = int(input())
bars = [int(sys.stdin.readline()) for _ in range(n)]

height = 0
cnt = 0

while bars:
  bar = bars.pop()
  if bar > height:
    cnt += 1
    height = bar

print(cnt)