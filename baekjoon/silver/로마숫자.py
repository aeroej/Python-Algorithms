import sys
si = sys.stdin.readline

# 일, 십, 백, 천의 자리
dicT = {
  3: ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX'],
  2: ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC'],
  1: ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM'],
  0: ['', 'M', 'MM', 'MMM'],
}


def rome_to_arabia(rome):
  num = 0
  flag = False

  for i in range(len(rome)):
    if flag:
      flag = False
      continue

    if rome[i] == 'M':
      num += 1000
    elif rome[i] == 'D':
      num += 500

    elif rome[i] == 'C':
      if rome[i+1] == 'D':
        num += 400
        flag = True
      elif rome[i+1] == 'M':
        num += 900
        flag = True
      else:
        num += 100

    elif rome[i] == 'L':
      num += 50

    elif rome[i] == 'X':
      if rome[i+1] == 'L':
        num += 40
        flag = True
      elif rome[i+1] == 'C':
        num += 90
        flag = True
      else:
        num += 10

    elif rome[i] == 'V':
      num += 5

    elif rome[i] == 'I':
      if rome[i+1] == 'V':
        num += 4
        flag = True
      elif rome[i+1] == 'X':
        num += 9
        flag = True
      else:
        num += 1

  return num


r1 = si().rstrip() + ' '
r2 = si().rstrip() + ' '
arabia = rome_to_arabia(r1) + rome_to_arabia(r2)
print(arabia)


num = ('000' + str(arabia))[-4:]
rome = ''

for i in range(4):
  rome += dicT[i][int(num[i])]

print(rome)
  