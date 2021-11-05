import sys
def input(): return sys.stdin.readline()

n = int(input())
seq = list(map(int, input().split()))

dp = [4992 * 1_000_000]*n
dp[0] = 0
dp[1] = 1 + abs(seq[1] - seq[0])

for i in range(2, n):
  for j in range(i):
    k = (i - j) * (1 + abs(seq[i] - seq[j]))
    dp[i] = min(dp[i], max(dp[j], k))

print(dp[n-1])




# 2의 5000승은 무한대..
# import sys
# def input(): return sys.stdin.readline()
# sys.setrecursionlimit(10**6)

# n = int(input())
# seq = list(map(int, input().split()))

# k = 1 + abs(seq[0] - seq[1])
# res = 5000 * 1_000_001


# def dfs(pre, depth, k):
#   global res
#   if depth == n-1:
#     new_k = max(k, (depth-pre)*(1 + abs(seq[pre] - seq[depth])))
#     res = min(res, new_k)
#     return

#   if k > res:
#     return

#   dfs(pre, depth + 1, k)  # 안 건넘
#   new_k = max(k, (depth-pre)*(1 + abs(seq[pre] - seq[depth])))
#   dfs(depth, depth + 1, new_k)  # 건넘


# dfs(0, 1, 0)
# print(res)





# 이분탐색 시도, dp 구현 실패
# import sys
# def input(): return sys.stdin.readline()
# sys.setrecursionlimit(10**6)


# def ispossible(mid):
#   idx = 0
#   while idx < n-1:
#     for i in range(idx + 1, n):
#       k = (i - idx) * (1 + abs(seq[idx] - seq[i]))
#       if k <= mid:
#         if i == n-1:
#           return True
#         idx = i
#         break
#       if i == n-1:
#         return False
#   return True


# n = int(input())
# seq = list(map(int, input().split()))

# left = 1
# right = 4992 * 1_000_000
# res = 5000 * 1_000_000

# while left <= right:
#   mid = (left + right) // 2

#   if ispossible(mid):
#     res = min(res, mid)
#     right = mid - 1
  
#   else:
#     left = mid + 1

  
# print(res)
  
