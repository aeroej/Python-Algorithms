import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
inputL = list(sys.stdin.readline().split())
sortL = sorted(inputL)
res = -1  # 오름차순 안되는 경우


visited = set("".join(inputL))  # 원소 : ''.join(<<list>>)
queue = deque([(inputL, 0)])

while queue:
    seqL, cnt = queue.popleft()
    if seqL == sortL:  # 종료조건 : 오름차순
        res = cnt
        break

    for i in range(n-k+1):  # k의 탐색범위
        tempL = seqL[:]
        tempL[i:i+k] = list(reversed(tempL[i:i+k]))

        word = "".join(tempL)
        if word not in visited:
            visited.add(word)
            queue.append((tempL, cnt+1))

print(res)
