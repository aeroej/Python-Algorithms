# 스택/큐

from collections import deque

def solution(priorities, location):
    queue = deque(priorities)
    max_p = max(queue)
    cnt = 0

    while True:
        if queue[0] == max_p:  # 인쇄
            cnt += 1
            if location == 0:
                return cnt
            queue.popleft()
            max_p = max(queue)
            
        else:
            queue.rotate(-1)

        if location == 0:
            location = len(queue) - 1
        else:
            location -= 1

    return
