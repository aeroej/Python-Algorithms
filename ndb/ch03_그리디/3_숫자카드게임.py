import sys
si = sys.stdin.readline

n, m = map(int, si().split())
min_cards = []

for _ in range(n):
  seq = list(map(int, si().split()))
  min_cards.append(min(seq))

print(max(min_cards))