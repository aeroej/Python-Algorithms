import sys

n = int(input())
p = list(map(int, sys.stdin.readline().rstrip().split()))
p.sort(reverse=True)

result = 0
for i in range(n):
  result += p[i]*(i+1)

print(result)