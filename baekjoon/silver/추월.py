import sys
def input(): return sys.stdin.readline().rstrip()

n = int(input())
start = [input() for _ in range(n)]
end = [input() for _ in range(n)]
res = set()

for i in range(n):
  for j in range(n):
    if start[i] == end[j]:
      res = res | (set(start[i+1:]) - set(end[j+1:]))
      break

print(len(res))
