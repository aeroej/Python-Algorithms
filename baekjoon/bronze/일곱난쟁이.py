import sys

height = sorted([int(input()) for _ in range(9)])
total = sum(height)

for i in range(8):
  for j in range(i+1, 9):
    if total - height[i] - height[j] == 100:
      for k in range(9):
        if k == i or k == j:
          continue
        print(height[k])
      sys.exit(0)
