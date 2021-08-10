import sys
from itertools import combinations

def city_length(shops):
  total = 0
  for house_x, house_y in houses:
    min_length = sys.maxsize
    for shop_x, shop_y in shops:
      length = abs(house_x - shop_x) + abs(house_y - shop_y)
      min_length = min_length if min_length < length else length
    total += min_length
  return total
      
if __name__ == '__main__':
  n, m = map(int, input().split())

  houses = []
  shops = []
  for i in range(n):
    line = input().split()
    for j in range(n):
      if line[j] == '1':
        houses.append([i, j])
      elif line[j] == '2':
        shops.append([i, j])

  result = sys.maxsize
  for shops in list(combinations(shops, m)):
    total = city_length(shops)
    result = result if result < total else total
  print(result)