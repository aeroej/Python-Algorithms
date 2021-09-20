import sys

n = int(sys.stdin.readline())
lst = [i for i in range(1, n+1)]  # 1, 2, 3, ...
seq = [int(sys.stdin.readline()) for _ in range(n)]  # 수열
stack = []
res = []  # output

while lst:
  l, s = lst[0], seq[0]
  if l < s:
    stack.append(lst.pop(0))
    res.append('+')

  elif l == s:
    stack.append(lst.pop(0))
    seq.pop(0)
    stack.pop()
    res.append('+')
    res.append('-')

  elif l > s:
    seq.pop(0)
    if s != stack.pop():
      print('NO')
      sys.exit(0)
    res.append('-')

while stack:
  if seq.pop(0) != stack.pop():
    print('NO')
    sys.exit(0)
  res.append('-')

print(*res, sep='\n')
