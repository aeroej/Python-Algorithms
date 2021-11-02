def solution(s):
    try:
        int(s)
        if len(s) == 4 or len(s) == 6:
            return True
        else:
            return False
    except Exception as e:  # 부적절한 값을 인자로 받았을 경우
        print(e)
        return False


solution('a1234234')
