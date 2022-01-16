import sys
si = sys.stdin.readline

n = int(si())
seq = [int(si()) for _ in range(n)]
print(*sorted(seq, reverse=True))