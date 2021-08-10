import sys

def recursion(num, rotation, vs): # 톱니 숫자, 톱니 회전방향, 톱니+1과 톱니-1 둘 중 누구와 비교
  if (0<num+vs<=4):
    if vs == 1:
      if graph[num][2] != graph[num+vs][6]:
        recursion(num+vs, -rotation, vs)
        handle_rotation(num+vs, -rotation)
    else:
      if graph[num][6] != graph[num+vs][2]:
        recursion(num+vs, -rotation, vs)
        handle_rotation(num+vs, -rotation)
  return "solution"

def handle_rotation(num, rotation):
  if rotation == 1:
    graph[num].insert(0, graph[num].pop())
  else:
    graph[num].append(graph[num][0])
    del graph[num][0]

if __name__ == "__main__":
  graph = [[0, 0, 0, 0, 0, 0, 0, 0]]
  for _ in range(4):
    graph.append(list(map(int, sys.stdin.readline().rstrip())))

  k = int(input())
  for _ in range(k):
    num, rotation = map(int, sys.stdin.readline().rstrip().split())
    recursion(num, rotation, 1)
    recursion(num, rotation, -1)
    handle_rotation(num, rotation)
  
  result = graph[1][0]
  result += graph[2][0]*2
  result += graph[3][0]*4
  result += graph[4][0]*8
  print(result)
    

# # 시계방향
# graph = deque([1, 2, 3, 4, 5])
# graph.insert(0, graph.pop())
# print(graph)

# # 반시계방향
# graph = deque([1, 2, 3, 4, 5])
# graph.append(graph.popleft())
# print(graph)