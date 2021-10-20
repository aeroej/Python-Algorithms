# import sys

# def dfs(stack):
#   if len(stack) == m:
#     stackT = tuple(stack)
#     if stackT not in total_stack:
#       print(*stack)
#       total_stack.add(stackT)
#     return

#   for i in range(n):
#     if visited[i] == 0:
#       visited[i] = 1
#       stack.append(seq[i])
#       dfs(stack)
#       visited[i] = 0
#       stack.pop()


# if __name__ == "__main__":
#   n, m = map(int, input().split())
#   seq = sorted(map(int, sys.stdin.readline().split()))

#   visited = [0]*n
#   total_stack = set()

#   dfs([])


import sys

n, m = map(int, input().split())
seq = sorted(map(int, sys.stdin.readline().split()))
visited = [0] * n
stack = []

def dfs(v):
    if v == m:
        print(*stack)
        return
        
    overlap = 0
    for i in range(n):
        if not visited[i] and overlap != seq[i]:
            visited[i] = 1
            stack.append(seq[i])
            overlap = seq[i]
            dfs(v+1)
            visited[i] = 0
            stack.pop()

dfs(0)
