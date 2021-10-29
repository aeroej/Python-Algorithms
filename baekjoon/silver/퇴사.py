# import sys

# def dfs(depth, money):
#   global max_money
#   if depth == n:  
#     max_money = max(max_money, money)
#     return
#   elif depth > n: 
#     return
  
#   t, p = table[depth]
#   dfs(depth+t, money + p) 
#   dfs(depth+1, money)
    

# if __name__ == "__main__":
#   n = int(input())
#   table = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
#   max_money = 0

#   dfs(0, 0)
#   print(max_money)



import sys

def dfs(depth, price):
  global max_price
  if depth == n:
    max_price = max(max_price, price)
    return

  if depth > n:
    return

  t, p = seq[depth]
  dfs(depth + t, price + p)
  dfs(depth + 1, price)


if __name__ == "__main__":
  n = int(input())
  seq = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

  max_price = 0
  dfs(0, 0)
  print(max_price)

