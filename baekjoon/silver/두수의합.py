import sys

n = int(input())
seq = sorted(list(map(int, sys.stdin.readline().split())))
x = int(input())

left, right = 0, n-1  # left +이동, right -이동
cnt = 0

while left < right :
  sum_seq = seq[left] + seq[right]
  
  if sum_seq == x:
    cnt += 1
    right -= 1
  elif sum_seq < x:
    left += 1
  elif sum_seq > x:
    right -= 1

print(cnt)