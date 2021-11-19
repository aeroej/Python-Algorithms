# # 순차 탐색, 시간 초과
# # 최악의 경우 : seq = [10000, 10000, 10000, 10000, ... 9999, 9998 9997, ... , 1]
# import sys
# def input(): return sys.stdin.readline()

# t = int(input())

# for _ in range(t):
#   n = int(input())
#   seq = list(map(int, input().split()))
#   total_price = 0

#   max_price = max(seq)

#   for i in range(n-1):
#     if seq[i] == max_price:
#       max_price = max(seq[i+1:])

#     else:
#       total_price += max_price - seq[i]


#   print(total_price)


import sys
def input(): return sys.stdin.readline()

t = int(input())

for _ in range(t):
  n = int(input())
  seq = list(map(int, input().split()))
  total_price = 0

  max_price = 0

  for i in range(n-1, -1, -1):
    if seq[i] > max_price:
      max_price = seq[i]

    else:
      total_price += max_price - seq[i]

  print(total_price)
