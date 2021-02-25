# sequence 멤버를 하나로 이어붙이기
# 문제 설명
# 문자열 리스트 mylist를 입력받아, 이 리스트의 원소를 모두 이어붙인 문자열을 리턴하는 함수, solution을 만들어주세요. 예를 들어 mylist가 ['1', '100', '33'] 인 경우, solution 함수는 '110033'을 리턴하면 됩니다.

# 제한 조건
# mylist의 길이는 100 이하인 자연수입니다.
# mylist의 원소의 길이는 100 이하인 자연수입니다.

# -------------------------------------------------------------

# 명답
mylist = ['1', '100', '33']
answer = ''.join(mylist)
print(answer)

# 설명
# 1. join() --> '삽입할문자'.join(리스트)
mylist = ['10', '20', '30']
answer = ';'.join(mylist)
print(answer)

# 2. split() --> 리스트.split('제거할문자')
mystr = '10/20/30'
answer = mystr.split('/')
print(answer)

# -------------------------------------------------------------

# 내 코드
def solution(mylist):
    answer = ''
    for list in mylist:
        answer += list
    return answer

if __name__ == '__main__':
    mylist = ['1', '100', '33']
    print(solution(mylist))
