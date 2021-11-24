import sys
from collections import defaultdict
def input(): return sys.stdin.readline()
sys.setrecursionlimit(10**6)
nodes = defaultdict(list)  # 인접리스트


n = int(input())
w = [0] + list(map(int, input().split())) # dummy value

for _ in range(n-1):
  parent, child = sorted(map(int, input().split()))
  nodes[parent].append(child)

dp = [[0, 0] for _ in range(n+1)]  # [노드가 포함되지 않은 가중치, 노드가 포함된 가중치]


def independent_set(n) -> list:
  set_f, set_t = [], [n]  # 노드가 포함되지 않은 / 포함된 독립집합
  dp[n][1] = w[n]

  if len(nodes[n]) == 0:  # leaf node
    return set_f, set_t

  for child in nodes[n]:
    chdset_f, chdset_t = independent_set(child)   # 자식노드가 포함되지 않은 / 포함된 독립집합

    # set_f
    if dp[child][0] > dp[child][1]:
      set_f += chdset_f
    else:
      set_f += chdset_t

    # set_t
    set_t += chdset_f

    dp[n][0] += max(dp[child])
    dp[n][1] += dp[child][0]

  return set_f, set_t


set_f, set_t = independent_set(1)

if dp[1][0] > dp[1][1]:
  print(dp[1][0])
  print(*sorted(set_f))  
else:
  print(dp[1][1])
  print(*sorted(set_t))
