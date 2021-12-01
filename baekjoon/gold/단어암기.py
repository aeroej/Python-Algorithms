import sys
def input(): return sys.stdin.readline().rstrip()

n, m = map(int, input().split())
bits = []
for _ in range(n):
  word = input()
  bit = 0

  for w in word:
    bit = bit | (1 << (ord(w) - ord('a')))
  bits.append(bit)

memory = (1 << 26) - 1  # 1111...11 : 1이 26개인 이진수
for _ in range(m):
  o, x = input().split()
  if o == "1":
    memory = memory ^ (1 << (ord(x) - ord('a')))
  elif o == "2":
    memory = memory | (1 << (ord(x) - ord('a')))
  
  cnt = 0
  for bit in bits:
    if memory | bit == memory:
      cnt += 1
  
  print(cnt)
