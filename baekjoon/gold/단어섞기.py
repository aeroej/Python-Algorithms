import sys
from collections import deque
def input(): return sys.stdin.readline()


n = int(input())
for _ in range(1, n+1):
  word1, word2, word3 = input().split()
  len1, len2, len3 = len(word1), len(word2), len(word1) + len(word2)
  visited = [[0]*201 for _ in range(201)]

  queue = deque([[0, 0]])

  while queue:
    idx1, idx2 = queue.popleft()

    if idx1 < len1 and word1[idx1] == word3[idx1 + idx2] and not visited[idx1][idx2]:
      queue.append([idx1 + 1, idx2])

    if idx2 < len2 and word2[idx2] == word3[idx1 + idx2] and not visited[idx1][idx2]:
      queue.append([idx1, idx2 + 1])

    visited[idx1][idx2] = 1

  if idx1 + idx2 == len3:
    print("Data set %d: yes" % (_)) #'{0}, {1}'.format(a, b)
  else:
    print("Data set %d: no" % (_))
