# 스택/큐

def solution(prices):
    leng = len(prices)
    res = [0]*leng

    for i in range(leng - 1):
        for j in range(i+1, leng):
            res[i] += 1
            if prices[i] > prices[j]:
                break

    return res
