import sys
input = lambda: sys.stdin.readline().rstrip()

n, m = map(int, input().split())
hear = set([input() for _ in range(n)])
see = set([input() for _ in range(m)])

res = sorted(hear.intersection(see))
print(len(res))

for i in range(len(res)):
  print(res[i])