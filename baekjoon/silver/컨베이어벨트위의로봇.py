import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
s = deque(map(int, sys.stdin.readline().split()))
robot = deque([0]*n)
idx = 0

def takeoff_robot():
  if robot[n-1] == 1:
    robot[n-1] = 0

while True:
  idx += 1
  # 1. 벨트와 로봇 회전
  s.rotate(1)
  robot.rotate(1)
  takeoff_robot()

  # 2. "가장 먼저 벨트에 올라간 로봇부터" 이동. 즉 역순으로 선형탐색
  for i in range(n-2, 0, -1):  # i와 i+1
    if robot[i] == 1 and robot[i+1] == 0 and s[i+1] > 0:
      robot[i] = 0
      robot[i+1] = 1
      s[i+1] -= 1
  takeoff_robot()
      
  # 3. 로봇 올림
  if robot[0] == 0 and s[0] > 0:
    robot[0] = 1
    s[0] -= 1

  # 4. 내구도 확인 후 break
  if s.count(0) >= k:
    break

print(idx)
