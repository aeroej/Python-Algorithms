# swap : 두 변수의 값 바꾸기
a = 10
b = 20
a, b = b, a
print(a, b)

# -------------------------------------------------------------

# binary search --> 이진 탐색 : 오름차순으로 정렬된 리스트에서 특정한 값의 위치를 찾는 알고리즘. 검색 속도가 아주 빠르다. 
import bisect

mylist = [1, 3, 5, 11, 33, 44, 55]
print(bisect.bisect(mylist, 33))

# -------------------------------------------------------------

# 클래스의 자동 string casting --> __str__ : 클래스 내부에서 인스턴스 출력 format 지정
class Coord(object):
    def __init__ (self, x, y):
        self.x, self.y = x, y
    def __str__ (self):
        return '({}, {})'.format(self.x, self.y)

point = Coord(1, 2)
print(point)

# -------------------------------------------------------------

# inf : 세상에서 가장 큰 수 --> 최솟값을 저장하는 변수에 아주 큰 값을 할당할 때 사용
min_val = float('inf')
print(min_val > 9999999999999999999999999999999999999999999999999)

min_val = float('-inf')
print(min_val < -9999999999999999999999999999999999999999999999999)

# -------------------------------------------------------------

# with as --> 간결한 파일 입출력

with open('divmod.py', 'rt', encoding='UTF8') as file:
    for line in file.readlines():
        print(line.strip().split('\t'))  # \t 탭 간격


