import sys
from collections import deque

n, w, l = map(int, sys.stdin.readline().split())
trucks = deque(list(map(int, sys.stdin.readline().split())))

bridge = deque([0]*w)
cnt = 0


while bridge:
  if trucks:
    if sum(bridge) - bridge[-1] + trucks[0] <= l:  # 트럭추가
      bridge.appendleft(trucks.popleft())
    else:
      bridge.appendleft(0)

  cnt += 1
  bridge.pop()


print(cnt)

