import sys

n = int(input())
graph = []
for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    graph.append([x, y])

for i in sorted(graph):
    print(i[0], i[1])
