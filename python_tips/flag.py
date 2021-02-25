# flag OR else
# 문제 설명
# 본 문제에서는 자연수 5개가 주어집니다.

# 숫자를 차례로 곱해 나온 수가 제곱수1가 되면 found를 출력하고
# 모든 수를 곱해도 제곱수가 나오지 않았다면 not found를 출력하는
# 코드를 작성해주세요.

# 예시 1
# 입력

# 2
# 4
# 2
# 5
# 1
# 출력
# found
# 설명

# 수를 곱해나가면 2, 8, 16, 80, 80 이 나옵니다.
# 16은 4를 제곱해 나온 수이므로, 이 수는 제곱수입니다.
# 따라서 found를 출력합니다.

# 예시 2
# 입력

# 5
# 1
# 2
# 3
# 1
# 출력

# not found
# 설명

# 수를 곱해나가면 5, 5, 10, 30, 30 이 나옵니다.
# 이중 어떤 수도 제곱 수가 아니므로 not found를 출력합니다.

# 제곱수란 어떤 자연수를 제곱한 수입니다. 예를 들어 1, 4, 9, 16, 25, .. 등은 제곱수입니다. ↩

# -------------------------------------------------------------

# 명답 : 내가 짠 코드랑 거의 비슷함 감격......! 
import math

numbers = [int(input()) for _ in range(5)]
multiplied = 1
for number in numbers:
    multiplied *= number
    if math.sqrt(multiplied) == int(math.sqrt(multiplied)):
        print('found')
        break
else:
    print('not found')

# 설명
# 1. square root 제곱근 구하기    1. num ** 0.5    2. math.sqrt()
# 2. 다수의 입력값을 Enter로 받기
# numbers = [int(input()) for _ in range(5)]
# for number in numbers:
# 3. _ 파이썬의 언더바 --> I don't care

# -------------------------------------------------------------

# 내 코드
def solution(mylist):
    num = 1
    for i in mylist:
        num *= i
        root = num ** 0.5
        if root == int(root):
            return "found"
    return "not found"

if __name__ == "__main__":
    mylist = []
    for i in range(5):
        a = int(input())
        mylist.append(a)
    print(solution(mylist))