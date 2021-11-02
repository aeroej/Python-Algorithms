import sys

def fibonacci(n):
  for i in range(len(cnt_0), n+1):
    cnt_0.append(cnt_0[i-1] + cnt_0[i-2])
    cnt_1.append(cnt_1[i-1] + cnt_1[i-2])
  print(cnt_0[n], cnt_1[n])


if __name__ == "__main__":
  t = int(sys.stdin.readline())
  cnt_0 = [1, 0]  # 0, 1, 0+1, 0+1+1, ...
  cnt_1 = [0, 1]

  for _ in range(t):
    n = int(sys.stdin.readline())
    fibonacci(n)



