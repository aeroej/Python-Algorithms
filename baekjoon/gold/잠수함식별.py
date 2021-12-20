# end idx, try except, pattern.fullmatch(string)
import sys
import re
si = sys.stdin.readline

sound = si().rstrip()
p = re.compile('(100+1+|01)+')
m = p.fullmatch(sound)

try:
  s, e = m.span()  # e = m.end() 대체가능

  if s == 0 and e == len(sound):
    print("SUBMARINE")
  else:
    print("NOISE")

except AttributeError:
  print("NOISE")





# if-else None, pattern.fullmatch(string)
import sys
import re
si = sys.stdin.readline

sound = si().rstrip()
p = re.compile('(100+1+|01)+')
m = p.fullmatch(sound)

if m:
  print("SUBMARINE")

else:
  print("NOISE")





# if-else None, re.fullmatch(pattern, string)
import sys
import re
si = sys.stdin.readline

sound = si().rstrip()
m = re.fullmatch('(100+1+|01)+', sound)

if m:
  print("SUBMARINE")

else:
  print("NOISE")
