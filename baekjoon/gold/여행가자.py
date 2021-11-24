import sys
def input(): return sys.stdin.readline()

n = int(input())
m = int(input())
p = [-1 for _ in range(n)]


def find(x):
  if p[x] < 0:  # 루트 노트
    return x
  
  p[x] = find(p[x])
  return p[x]


def union(x, y):
  x = find(x)
  y = find(y)

  if x == y:
    return

  if p[x] > p[y]:  # y의 집합의 원소개수가 더 많다 (음수)
    p[y] += p[x]  # x의 집합을 y의 집합에 합류 (-집합의 개수)
    p[x] = y  # x는 더이상 루트노드가 아님 (음수가 아님), x의 루트 노드를 갱신
  else:
    p[x] += p[y]
    p[y] = x


for i in range(n):
  graph = list(map(int, input().split()))
  for j in range(n):
    if graph[j] == 1:  # 연결된 도시, 분리집합
      union(i, j)

plan = list(map(int, input().split()))
flag = "YES"
root = find(plan[0] - 1)

for i in range(m):  # 여행계획도시들이 같은 집합에 포함되어있는지, 모두 루트노드가 같은지
  if root != find(plan[i] - 1):
    flag = "NO"
    break

print(flag)


