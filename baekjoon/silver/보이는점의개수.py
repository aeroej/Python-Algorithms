import sys

res = [0]*1001
res[1] = 3

def gcd(a, b):
  while b != 0:
    a, b = b, a%b
  return a

for i in range(2, 1001):
  cnt = 0
  for j in range(1, i+1):  # (n, 0) ~ (n, n) 영역
    if gcd(i, j) == 1:
      cnt += 1
  res[i] = res[i-1] + cnt * 2

c = int(input())
for _ in range(c):
  inpuT = int(sys.stdin.readline())
  print(res[inpuT])
