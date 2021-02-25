# 가장 많이 등장하는 알파벳 찾기
# 문제 설명
# 이 문제에는 표준 입력으로 문자열, mystr이 주어집니다. mystr에서 가장 많이 등장하는 알파벳만을 사전 순으로 출력하는 코드를 작성해주세요.

# 제한 조건
# mystr의 원소는 알파벳 소문자로만 주어집니다.
# mystr의 길이는 1 이상 100 이하입니다.
# 예시
# input	output
# 'aab'	'a'
# 'dfdefdgf' 'df'
# 'bbaa' 'ab'

# -------------------------------------------------------------

# 명답
import collections

my_str = input().strip()
dic = collections.Counter(list(my_str))
maximum = max(dic.values())
result = filter(lambda x:x[1] == maximum, dic.items())
answer = [key for key, value in result]
answer.sort()
print(''.join(answer))

# 설명
# list() dict()에 집착하지 않다니,,, 출력이 안되는데도,,, 이거슨 센세이션...
# 1. collection.Couter(iternal) --> key가 iternal이고 value가 키의 등장횟수인 Dictionary
# 2. filter(함수, 반복인자) --> dic.items()은 ('a', 3) tuple type --> lambda x:x[1]에서, x는 ('a', 3), x[1]는 3 value값
# 3. value가 maximum인 dictionary item 필터링 --> key만 필터링 --> sort 정렬 --> 배열을 문자열로 join

# -------------------------------------------------------------

# 설명
# 1. dict.fromkeys(iternal) --> key는 iternal이고 value는 null인 dictionay 생성
# string.ascii_lowercase --> 'abcde...xyz'
# 2. list = sorted(iternal) --> iternal.sort()와는 달리 원본유지
# 3. lambda x : X --> 원본유지
a = lambda x , y : x * y 
print( a(3, 4) )

a = [ -1, -8, 3, -4, 2, 5, -7]
b = sorted(a, key=lambda x : x*x, reverse=True) # 제곱값이 큰 수부터 내림차순 정렬
print( b )

# 내 코드 
import string

my_str = input().strip()
answer = ''

dicts = dict.fromkeys(string.ascii_lowercase, 0) # alphabet dictionary
    
for key in my_str :
    dicts[key] += 1

sorted_dict = sorted(dicts.items(), key=lambda x:x[1], reverse=True) # 내림차순 정렬, sorted_dict은 tuple type, x[1] 즉 value가 큰수부터 정렬

max = sorted_dict[0][1] # 첫번째 value = Max value

for tuple in sorted_dict: # sorted_dict은 tuple type
    if tuple[1] < max: # tuple[1]은 value
        break
    answer += tuple[0] # tuple[0]은 key

print(answer)