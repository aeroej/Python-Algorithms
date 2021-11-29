limit = 1_003_002

n = int(input())
seq = [1] * limit  # 모두 소수일 가능성 있음


def is_palindrome(num):
  if str(num) == str(num)[::-1]:
    return True
  return False


for i in range(3, limit, 2):  # 짝수는 확인할 필요가 없음
  if n == 1 or n == 2:
    print(2)
    break

  if seq[i]:  # 아직 탐색 전인 수의 경우 == 소수, 그 수의 배수는 0 처리
    if i >= n and is_palindrome(i):
      print(i)
      break
    for j in range(i*2, limit, i):  # 3, 6, 9, .. 배수
      seq[j] = 0
