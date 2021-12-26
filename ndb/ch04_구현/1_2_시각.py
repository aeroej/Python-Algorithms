import sys
si = sys.stdin.readline

# hour에 3이 포함된 경우
# 60 * 60 = 3600만큼 더하기

# hour에 3이 포함되지 않는 경우
# 미리 구한 cnt만큼 더하기

cnt = 0
for i in range(60):
  for j in range(60):
    if '3' in str(i) + str(j):
      cnt += 1

n = int(si())
res = 0

for i in range(n + 1):
  if '3' in str(i):
    res += 3600
  else:
    res += cnt

print(res)