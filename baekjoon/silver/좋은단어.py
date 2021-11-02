import sys

n = int(input())
res = 0
for _ in range(n):
  word = sys.stdin.readline().rstrip()
  for _ in range(len(word)//2):
    if word == '':
      break
    word = word.replace('AA', '')
    word = word.replace('BB', '')

  if word == '':
    res += 1

print(res)



