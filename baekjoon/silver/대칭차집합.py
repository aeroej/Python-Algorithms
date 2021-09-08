import sys

num_a, num_b = map(int, input().split())
a = set(map(int, sys.stdin.readline().split()))
b = set(map(int, sys.stdin.readline().split()))

print(len(a-b) + len(b-a))
# print(len(a^b))