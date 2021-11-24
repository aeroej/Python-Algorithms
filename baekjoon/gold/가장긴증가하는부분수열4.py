# # filter
# import sys
# from collections import deque
# def input(): return sys.stdin.readline()

# n = int(input())
# A = list(map(int, input().split()))
# dp = [1]*n

# for i in range(1, n):
#   tmp = 0
#   idx_list = list(filter(lambda x: A[x] < A[i], range(i)))

#   if idx_list:
#     idx_max = max(idx_list, key=lambda x: dp[x])
#     dp[i] = dp[idx_max] + 1


# res = deque([])
# target = max(dp)

# for i in range(n-1, -1, -1):
#   if dp[i] == target:
#     target -= 1
#     res.appendleft(A[i])


# print(len(res))
# print(*res)


from collections import deque
N = int(input())
A = list(map(int, input().split()))
dp = [1] * N
Alist = [[] for i in range(N)]

for i in range(N):
    tmp = []
    for j in range(i):
        if A[j] < A[i]:
            if dp[j]+1 >= dp[i]:

                if dp[j]+1 == dp[i]:
                    tmp.pop(len(tmp)-1)
                tmp.append(A[j])

                dp[i] = dp[j]+1
    tmp.append(A[i])
    Alist[i] = tmp

print(max(dp))
print(*Alist[dp.index(max(dp))])
