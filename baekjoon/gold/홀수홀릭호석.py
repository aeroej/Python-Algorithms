import sys

def recursion(num, cnt_odd):
  if len(num) == 1:
    cnt_odd += int(num) % 2
    res[0] = min(res[0], cnt_odd)
    res[1] = max(res[1], cnt_odd)

  elif len(num) == 2:
    cnt_odd += sum(map(lambda x: int(x) % 2, num))
    new_num = str(int(num[0]) + int(num[1]))
    recursion(new_num, cnt_odd)
  
  else: 
    cnt_odd += sum(map(lambda x: int(x) % 2, num))  # '12345' -> [1, 0, 1, 0, 1]
    for i in range(1, len(num) - 1):
      for j in range(i + 1, len(num)):
        new_num = str(int(num[:i]) + int(num[i:j]) + int(num[j:]))
        recursion(new_num, cnt_odd)

  return


n = sys.stdin.readline().rstrip()
res = [int(n), 0]
recursion(n, 0)
print(*res)
