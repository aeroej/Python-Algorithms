import sys
def input(): return sys.stdin.readline()

n = int(input())
seq = sorted(map(int, input().split()))

left = 0
right = n-1
res = [1e10]*3

while left < right:
  suM = seq[left] + seq[right]
  if res[0] > abs(suM):
    res[0] = abs(suM)
    res[1], res[2] = seq[left], seq[right]
  if suM > 0:
    right -= 1
  elif suM < 0:
    left += 1
  elif suM == 0:
    break

print(res[1], res[2])

