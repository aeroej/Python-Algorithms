import sys
def input(): return sys.stdin.readline()

t = int(input())
for _ in range(t):
  n = int(input())
  seq = list(map(int, input().split()))

  for i in range(1, n):
    seq[i] = max(seq[i], seq[i-1] + seq[i])

  print(max(seq))

