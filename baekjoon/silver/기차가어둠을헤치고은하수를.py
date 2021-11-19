import sys
def input(): return sys.stdin.readline().split()


n, m = map(int, input())
trains = [0] + [(1 << 20) for _ in range(n)]

for _ in range(m):
  c, *num = map(int, input())
  if c == 1:
    i, x = num
    trains[i] = trains[i] | (1 << x-1)
  elif c == 2:
    i, x = num
    trains[i] = trains[i] & ~(1 << x-1)
  elif c == 3:
    i = num[0]
    trains[i] = (trains[i] << 1) | (1 << 20)
    trains[i] -= 2 ** 21
  elif c == 4:
    i = num[0]
    trains[i] = (trains[i] >> 1) | (1 << 20)
    trains[i] -= 2 ** 19

print(len(set(trains)) - 1)
