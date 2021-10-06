import sys

def solution(oper: str, n: int, s: int) -> int:
  if oper == 'add':
    return s | (1 << n)
  elif oper == 'remove':
    return s & ~(1 << n)
  elif oper == 'check':
    print(bin(s & (1 << n))[2:3]) 
    return s
  elif oper == 'toggle':
    return s ^ (1 << n)


if __name__ == '__main__':
  m = int(input())
  s = 0

  for _ in range(m):
    inpuT = sys.stdin.readline().split()

    if inpuT[0] == 'all':
      s = 2_097_150  # bin(2_097_150) == str '0b111111111111111111110'
    elif inpuT[0] == 'empty':
      s = 0
    else:
      s = solution(inpuT[0], int(inpuT[1]), s)
      


# print(bin(2_097_150) == '0b111111111111111111110') # ouput type : str

# print(int('1010')) # input type : int, str  
# print(int('1010', 10))  # input type : only str
# # TypeError: int() can't convert non-string with explicit base
# # 10진수의 기수(base)는 10이다.

# print(int('11', 2)) # 2진수를 10진수로 convert
# print(int('0b11', 2)) # 2진수를 10진수로 convert

