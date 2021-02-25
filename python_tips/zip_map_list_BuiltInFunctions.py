# 2차원 리스트 뒤집기
# 문제 설명
# 다음을 만족하는 함수, solution을 완성해주세요.

# solution 함수는 이차원 리스트, mylist를 인자로 받습니다
# solution 함수는 mylist 원소의 행과 열을 뒤집은 한 값을 리턴해야합니다.
# 예를 들어 mylist [ [1,2,3], [4,5,6], [7,8,9] ]가 주어진 경우, solution 함수는 [[1, 4, 7], [2, 5, 8], [3, 6, 9]] 을 리턴하면 됩니다.

# 제한 조건
# mylist의 원소의 길이는 모두 같습니다.
# mylist의 길이는 mylist[0]의 길이와 같습니다.
# 각 리스트의 길이는 100 이하인 자연수입니다.

# ----------------------------------------------------------------

# 명답
# 1. mylist를 zip해서 같은 인덱스에 있는 원소들만 모아주고싶어. 
# 2. 그런데 리스트 안에 리스트 구조니까 * upzip을 해줘야겠군.
# 3. 그런데 zip(*mylist) --> (1, 4, 7) (2, 5, 8) (3, 6, 9) 리스트 안에 리스트로 묶이질 않잖아?
# 4. map()덕분에 list( (1, 4, 7) ),  list( (2, 5, 8) ), list( (3, 6, 9) ) 수행 --> [1, 4, 7] [2, 5, 8] [3, 6, 9] 생성
# 5. 최종 리스트 껍데기 감싸주기 list(   map(list, zip(*mylist))   )
mylist = [ [1,2,3], [4,5,6], [7,8,9] ]
print(list(   map(list, zip(*mylist))   ))

# ----------------------------------------------------------------

# 설명
# 1. zip() : 같은 index에 있는 iterables 원소를 모음  --> 성의없게 ()로 묶음 & 껍데기 없음
# zip('ABCD', 'xy') --> Ax By --> ('A', 'x') ('B', 'y')
# * : 리스트 안에 리스트는 꼭 unzip해줘야 한다!!! 껍데기를 벗겨줘야 한다!!!
print(list(   zip(*mylist)   ))
print(list(   zip(mylist, [10, 20, 30])   )) # *가 없으면 걍 얘랑 얘랑 묶어야지~! 수행

# 2. map(함수, 반복할 인자) --> 함수(인자), 함수(인자), ...  -->  성의없게 껍데기 없음
# 반복할 인자 껍데기 o
users = [{'name': 'Brett Holland', 'sex': 'M'}, {'name': 'Madison Martinez', 'sex': 'F'}, {'name': 'Michael Jenkins', 'sex': 'M'}, {'name': 'Amber Rhodes', 'sex': 'F'}]

def conver_to_name(user):
    first, last = user["name"].split()
    return {"first": first, "last": last}

print(list(   map(conver_to_name, users)   ))  # cover_to_name(user), cover_to_name(user), ...

# 3. list(반복자료형) : 반복가능한 자료형을 입력받아 리스트로 만들어줌
print(list("python"))
print(list( (1, 2, 3) ))

# +. for index, value in enumerate(list) : 

# ----------------------------------------------------------------

# 내 코드
def solution(mylist):
    answer = []

    for i in mylist:
        answer.append([])

    for list in mylist:    
        for index, value in enumerate(list) :
            answer[index].append(value)
    return answer

print(solution([ [1,2,3], [4,5,6], [7,8,9] ]))

