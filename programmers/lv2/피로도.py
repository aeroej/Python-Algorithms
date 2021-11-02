# 위클리 챌린지

res = 0

def solution(k, dungeons):
    global res
    visited = [0]*len(dungeons)
    dfs(k, dungeons, visited)
    return res


def dfs(hp, dungeons, visited):
    global res
    res = max(res, sum(visited))

    for i in range(len(dungeons)):
        if hp >= dungeons[i][0] and not visited[i]:
            visited[i] = 1
            dfs(hp - dungeons[i][1], dungeons, visited)
            visited[i] = 0
