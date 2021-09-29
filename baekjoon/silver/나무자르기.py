import sys
input = sys.stdin.readline


def take_tree(num):
  tree = 0
  for i in range(n):
    tree += trees[i]-num if trees[i]-num > 0 else 0
  return tree


if __name__ == "__main__":
  n, m = map(int, input().split())
  trees = list(map(int, input().rstrip().split()))

  left, right = 0, max(trees)
  max_h = 0

  while left <= right:
    mid = (left + right)//2
    tree = take_tree(mid)

    if tree == m:
      max_h = mid
      break
    elif tree > m:
      max_h = mid if max_h < mid else max_h
      left = mid + 1
    else:
      right = mid - 1

  print(max_h)
    
  



