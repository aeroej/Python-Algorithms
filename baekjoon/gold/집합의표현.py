import sys
sys.setrecursionlimit(10**6)
def input(): return sys.stdin.readline().split()

def find(a):
  if parent[a] == a:
    return a
  
  parent[a] = find(parent[a])

  return parent[a]


def union(a, b):
  a = find(a)
  b = find(b)

  if a > b:
    parent[b] = a
  else:
    parent[a] = b
  return


n, m = map(int, input())
parent = [_ for _ in range(n+1)]

for _ in range(m):
  num, a, b = map(int, input())
  if num == 0:
    union(a, b)
  else:
    if find(a) == find(b):
      print("YES")
    else:
      print("NO")
      
    

