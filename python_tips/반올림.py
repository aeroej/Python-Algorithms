# https://dpdpwl.tistory.com/94

# 반올림 : round(실수, 표현하고싶은 자릿수)
n = 1.666666666667
print(round(n, 2))
print(round(n))
print(round(n, -1)) # 정수 반올림


# 올림, 내림 : math
import math

print(math.ceil(1.33))
print(math.floor(1.67))
