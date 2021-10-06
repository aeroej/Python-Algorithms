# import sys
# from collections import deque

# def solution(queue):
#   stack = []
#   while queue:
#     q = queue.popleft()
#     if q == '(':
#       stack.append(q)
#     else:
#       if len(stack) == 0:
#         return "NO"
#       stack.pop()
  
#   return "NO" if len(stack) else "YES"


# if __name__ == "__main__":
#   t = int(input())
#   for _ in range(t):
#     queue = deque(list(map(str, sys.stdin.readline().strip())))
#     print(solution(queue))



import sys

def solution(ps):
  num = 0
  for i in ps:
    if i == '(':
      num += 1
    elif i == ')':
      num -= 1
      if num < 0:
        return 'NO'
      
  return 'NO' if num else 'YES'


if __name__ == "__main__":
  t = int(input())
  for _ in range(t):
    print(solution(sys.stdin.readline().strip()))
