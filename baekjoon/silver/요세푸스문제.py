from collections import deque

n, k = map(int, input().split())
queue = deque([_ for _ in range(1, n+1)])

print('<', end='')

while queue:
  for i in range(1, k+1):
    man = queue.popleft()
    if i == k:
      if len(queue) == 0:
        print(man, end='>')
        break
      print(man, end=', ')
      break
    queue.append(man)
