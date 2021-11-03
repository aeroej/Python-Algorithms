import sys

# input() 재정의
input = lambda: sys.stdin.readline()
def input(): return sys.stdin.readline()


# input() 
## 1. \n 행간을 제거한 값을 할당
## 2. 프롬프트 매개변수 있음 --> input("명령어를 입력해주세요. ")

# sys.stdin.readline()
## 1. \n 행간을 제거하지 않고 할당
### 1) 문자열을 사용하는 경우 rstrip() 작성
### 2) int 변환 또는 split() 하는 경우 rstrip() 생략
## 2. 프롬프트 매개변수 없음 

# 두 가지 이유로 sys.stdin.readline()의 성능이 더 뛰어남
