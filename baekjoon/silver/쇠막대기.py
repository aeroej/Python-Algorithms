import sys

n = sys.stdin.readline().strip()
stick = 0
answer = 0

for i in range(len(n)):
    if n[i] == '(':
        stick += 1
        answer += 1
    elif n[i] == ')':
        stick -= 1
        if n[i-1] == '(':  # 레이저인 경우
            answer += stick - 1

print(answer)

