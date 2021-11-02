import sys
import re

n = int(input())
math = sys.stdin.readline().rstrip()

digit = list(map(int, re.sub('[A-Z]', ' ', math).split()))
oper = re.sub('[0-9]', '', math)

num = digit[0]
idx = 1
res = []

for i in range(n):
  if oper[i] == 'C':
    res.append(num)
    continue
  try:
    if oper[i] == 'S':
      num -= digit[idx]
    elif oper[i] == 'M':
      num *= digit[idx]
    elif oper[i] == 'U':
      num = int(num / digit[idx])
    elif oper[i] == 'P':
      num += digit[idx]
    idx += 1
  except IndexError:  
    if res:
      print(*res)
    else:
      print("NO OUTPUT")
    sys.exit(0)

if res:
  print(*res)
else:
  print("NO OUTPUT")



# print(*res if res else 'NO OUTPUT')  # output: N O   O U T P U T





# # 빡구현
# import sys

# n = int(input())
# math = sys.stdin.readline().rstrip()
# res = []

# digit0 = 0
# alpha0 = 'P'
# start = 0

# for i in range(len(math)):
#   if math[i].isalpha():
#     if alpha0 == 'C':
#       digit1 = digit0
#     else:
#       digit1 = int(math[start:i])

#       if alpha0 == 'S':
#         digit1 = digit0 - digit1
#       elif alpha0 == 'M':
#         digit1 = digit0 * digit1
#       elif alpha0 == 'U':
#         digit1 = digit0 // digit1 if digit0 > 0 else -(abs(digit0) // digit1)
#       elif alpha0 == 'P':
#         digit1 = digit0 + digit1

#     alpha1 = math[i]
#     if alpha1 == 'C':
#       res.append(digit1)

#     digit0 = digit1
#     alpha0 = alpha1
#     start = i+1

# if res:
#   print(*res)
# else:
#   print('NO OUTPUT')
