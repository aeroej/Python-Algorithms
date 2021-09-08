import sys

num_a, num_b = map(int, input().split())
a = set(map(int, sys.stdin.readline().split()))
b = set(map(int, sys.stdin.readline().split()))

diff = sorted(a-b)
print(len(diff))
print(*diff)
# Asterisk


