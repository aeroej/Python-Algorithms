# 몫과 나머지

# 숫자 a, b가 주어졌을 때 a를 b로 나눈 몫과 a를 b로 나눈 나머지를 공백으로 구분해 출력해보세요.

# 입력 설명
# 입력으로는 공백으로 구분된 숫자가 두 개 주어집니다.
# 첫 번째 숫자는 a를 나타내며, 두 번째 숫자는 b를 나타냅니다.

# 출력 설명
# a를 b로 나눈 몫과 a를 b로 나눈 나머지를 공백으로 구분해 출력하세요.

# 제한 조건
# a와 b는 자연수입니다.


a, b = map(int, input().strip().split(' '))
print(int(a/b), a%b)
print(a//b, a%b)

print(divmod(a, b))
print(*divmod(a, b))