# import sys
# from collections import deque

# n = int(input())
# seq = deque(sorted(map(int, sys.stdin.readline().split())))


# def dfs():
#   if len(seq) < 3:
#     return len(seq)
#   if seq[0] + seq[1] > seq[-1]:
#     return len(seq)
  
#   temp = seq.popleft()
#   dfs()
#   seq.appendleft(temp)
#   seq.pop()
#   dfs()

# print(dfs())




import sys

n = int(input())
seq = sorted(map(int, sys.stdin.readline().split()))
res = 0

for i in range(n-2):
  for j in range(n-1, i, -1):
    if seq[i] + seq[i+1] > seq[j]:
      res = max(res, j-i+1)
      break

if len(seq) < 3:
  res = len(seq)

print(res)
