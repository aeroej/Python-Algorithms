import sys

n = int(input())
graph = []
for _ in range(n):
    x, y = sys.stdin.readline().split()
    graph.append([int(x), y])

for i in sorted(graph, key=lambda x: x[0]):
    print(i[0], i[1])
