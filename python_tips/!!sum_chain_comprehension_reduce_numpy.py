# 2차원 리스트를 1차원 리스트로 만들기
# 문제 설명
# 문자열을 담은 이차원 리스트, mylist 가 solution 함수의 파라미터로 주어집니다. solution 함수가 mylist를 일차원 리스트로 만들어 리턴하도록 코드를 작성해주세요.

# 제한 조건
# arr의 길이는 1 이상 100 이하인 자연수입니다.
# arr 원소의 길이는 5를 넘지 않습니다.
# 예시
# input	output
# [[1], [2]]	[1, 2]
# [['A', 'B'], ['X', 'Y'], ['1']]     ['A', 'B', 'X' ,'Y', '1']

# -------------------------------------------------------------

# 일반 : 리스트 더하기
my_list = [[1, 2], [3, 4], [5, 6]]
answer = []
for i in my_list:
    answer += i
print(answer)

# 명답1 : sum() 이중리스트 합치기 --> 두번째 인자 사용해야 함
print(  sum(my_list, [])  )

sumList = [1, 2, 3, 4, 5]  # sum()의 원래용도 : 인자끼리 더하기
print(  sum(sumList)  )

# 명답2 : chain()
import itertools
print(  list(itertools.chain('ABC', 'DEF'))  )  # chain('ABC', 'DEF') --> A B C D E F --> 원래 여러 리스트를 대상으로 함

print(  list(itertools.chain(*my_list))  )  # zip과 유사하다. NO껍데기 & 이중리스트는 upzip * 필요함

print(  list(itertools.chain.from_iterable(my_list))  )

# 명답3 : list comprehension
# my_list의 요소 array에서, array의 요소 element를 가지고 []껍데기 감싸주기
# element for array in my_list
#     for element in array
print(  [element for array in my_list for element in array]  )
print(  list(element for array in my_list for element in array)  )

# 명답4 : reduce()
from functools import reduce
list(reduce(lambda x, y: x+y, my_list))

from functools import reduce
import operator
list(reduce(operator.add, my_list))

# 명답 5 : numpy flatten
# [['A', 'B'], ['X', 'Y'], ['1’]] 처럼 각 원소의 길이가 다른 리스트는 편평하게 만들 수 없다
# import numpy as np
# np.array(my_list).flatten().tolist()

# -------------------------------------------------------------

# 내 코드
def solution(mylist):
    answer = []
    for list in mylist:
        for i in list:
            answer.append(i)
    return answer

if __name__ == '__main__':
    mylist = [['A', 'B'], ['X', 'Y'], ['1']]
    print(solution(mylist))

