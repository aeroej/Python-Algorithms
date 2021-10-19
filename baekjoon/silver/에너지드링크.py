import sys

n = int(input())
seq = sorted(map(int, sys.stdin.readline().split()), reverse=True)
print(seq[0] + sum(seq[1:])/2)  