# -------------------------------------------------------------

# 명답
import itertools

iterable1 = 'ABCD'
iterable2 = '1234'
iterable3 = 'xy'

answer = itertools.product(iterable1, iterable2, iterable3)
print(list(answer))

# 설명
# 1. Cartesian product 곱집합 구하기
# 'ABCD', 'xy' 의 곱집합 --> Ax Ay Bx By Cx Cy Dx Dy
# 2. itertools.product() --> 성의없이 껍데기없음 --> list() 껍데기주기

# -------------------------------------------------------------

