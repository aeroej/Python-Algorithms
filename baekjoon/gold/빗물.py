import sys
def input(): return sys.stdin.readline().split()

h, w = map(int, input())
block = list(map(int, input()))
water = 0

for height in range(max(block), 0, -1):
  idx = -1

  for i in range(0, w):
    if block[i] >= height:
      empty = i - idx - 1
      if empty > 0 and idx > -1:
        water += empty

      idx = i

print(water)
