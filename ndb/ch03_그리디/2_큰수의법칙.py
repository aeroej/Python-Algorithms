import sys
import heapq
si = sys.stdin.readline

def solution() -> int:
  fst = -heapq.heappop(q)
  snd = -heapq.heappop(q)

  if fst == snd:
    return fst * m

  cnt_snd = int(m / (k + 1))
  cnt_fst = m - cnt_snd

  return (cnt_fst * fst + cnt_snd * snd)


n, m, k = map(int, si().split())
q = list(map(lambda x: -int(x), si().split()))
heapq.heapify(q)

print(solution())
