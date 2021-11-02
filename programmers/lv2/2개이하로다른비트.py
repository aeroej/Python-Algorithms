# 월간 코드 챌린지 시즌2

def solution(numbers):
    result = []

    for number in numbers:
        bi = '0' + bin(number)[2:]

        if bi[-1] == '0':
            bi = bi[:-1] + '1'

        else:
            for i in range(len(bi) - 1, -1, -1):
                if bi[i] == '0':
                    bi = bi[:i] + '10' + bi[i+2:]
                    break

        result.append(int(bi, 2))

    return result
