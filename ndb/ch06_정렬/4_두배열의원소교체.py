import sys
si = sys.stdin.readline

n, k = map(int, si().split())
a = list(map(int, si().split()))
b = sorted(map(int, si().split()))

a += b[-k:]
print(sum(sorted(a, reverse=True)[:n]))
