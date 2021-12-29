import sys
si = sys.stdin.readline
 

n = int(si())

visited = [0] * (n + 1)
prime = [2]


for i in range(3, n + 1, 2):
  if visited[i] == 0:
    prime.append(i)
    
    for j in range(i * 2, n + 1, i):
      visited[j] = 1


res = 0
s, e = 0, 0
add = prime[0]

while s <= e < len(prime):
  if add == n:
    res += 1
    add -= prime[s]
    s += 1
    
  elif add > n:  
    add -= prime[s]
    s += 1

  elif add < n: 
    e += 1
    if e == len(prime):
      break
    add += prime[e]


print(res)
