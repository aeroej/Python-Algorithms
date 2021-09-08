import sys
import collections

inpuT = sorted(sys.stdin.readline().rstrip())
dicT = collections.Counter(inpuT)

odd = list(filter(lambda x: x[1] % 2 == 1, dicT.items()))  # tuple [('C', 1)]
middle = ''

if len(odd) > 1:
  print("I'm Sorry Hansoo")
  sys.exit(0)
elif len(odd) == 1:
  middle = odd[0][0] # key 'C'

result = ''
for key, val in dicT.items():
    result += key*(val//2)

print(result + middle + result[::-1])

