# import sys
# from collections import deque

# seq = sys.stdin.readline()
# queue = deque([0])

# for x in seq:
#   if x.isdigit():
#     queue[-1] = (queue[-1])*10 + int(x)
#   elif x in '+-':
#     queue.append(x)
#     queue.append(0)


# while '+' in queue:
#   x = queue.popleft()

#   if x == '+':
#     queue[-1] += queue.popleft()
#   else:
#     queue.append(x)
# print(queue)

# res = queue[0]
# for x in range(2, len(queue), 2):
#   res -= queue[x]

# print(res)




import sys

seq = sys.stdin.readline().rstrip().split('-')
res = 0

for i in range(len(seq)):
  if '+' in seq[i]:
    temp = 0
    for x in seq[i].split('+'):
      temp += int(x)
    seq[i] = temp

  if i == 0:
    res += int(seq[i])
  else:
    res -= int(seq[i])

print(res)
