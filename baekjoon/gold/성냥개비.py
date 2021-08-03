arr = ['0', '0', '1', '7', '4', '2', '6', '8', '10', '18', '22', '20', '28', '68', ]

def max_number(n):
  if n <= 3:
    return arr[n]  # 일의 자리
  if n%2:  # 가장 큰 자릿수에 '7'
    result = '7'
  else:  # 가장 큰 자릿수에 '1'
    result = '1'
  for _ in range(int(n/2)-1):
    result += '1'
  return result

def min_number(n):
  if n <= 7:
    return arr[n]  # 일의 자리
  result = '1'
  n -= 2
  quot = int(n/6)
  remain = n%6
  if remain <= 1:
    quot -= 1
    remain += 6
  for _ in range(quot):
    result += '0'
  result += arr[remain]
  return result

t = int(input())
for _ in range(t):
  n = int(input())
  print(int(min_number(n)), int(max_number(n)))