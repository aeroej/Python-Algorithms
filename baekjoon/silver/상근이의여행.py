import sys
from collections import deque

if __name__ == '__main__':
  t = int(input())
  for _ in range(t):
    n, m = map(int, input().split())
    for _ in range(m):
      x, y = map(int, input().split())
    print(n-1)
    
