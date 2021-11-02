n = int(input())
res = []
while n>0:
  res.insert(0, n%2)
  n = n//2
print(''.join(map(str, res)))
# 역순으로 출력 res[::-1]
# print(*li, sep='')
