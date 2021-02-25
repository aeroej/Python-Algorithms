# 모든 멤버의 type 변환하기
# 문제 설명
# 문자열 리스트 mylist를 입력받아, 이 리스트를 정수형 리스트로 바꾼 값을 리턴하는 함수, solution을 만들어주세요. 예를 들어 mylist가 ['1', '100', '33'] 인 경우, solution 함수는 [1, 100, 33] 을 리턴하면 됩니다.

# 제한조건
# mylist의 길이는 100 이하인 자연수입니다.
# mylist의 원소는 10진수 숫자로 표현할 수 있는 문자열입니다. 즉, 'as2' 와 같은 문자열은 들어있지 않습니다.
# 예시
# input	output
# ['1', '100', '33']	[1, 100, 33]

# -------------------------------------------------------------

# 명답

def solution(mylist):
    answer = []
    return list(map(int, mylist))

if __name__ == '__main__':
    mylist = ['1', '100', '33']
    print(solution(mylist))

# 설명
# 1. map(함수, 반복할 인자) --> 함수(인자1), 함수(인자2), 함수(인자3), ... --> 불친절하여 껍데기없음
# 2. list(반복할 자료형) --> 반복되는 자료형들을 입력받아 리스트로 만들어줌 --> 불친절한 map 대신 껍데기 만들어줌

# -------------------------------------------------------------

# 내 코드
def solution(mylist):
    answer = []
    for list in mylist: 
        answer.append(int(list))
    return answer

if __name__ == '__main__':
    mylist = ['1', '100', '33']
    print(solution(mylist))
