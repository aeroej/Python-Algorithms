n, k = map(int, input().split())
shirts = list(map(int, input().split()))
diff = []

for i in range(n-1):
  diff.append(shirts[i+1]-shirts[i])

diff.sort()
print(sum(diff[:n-k]))
