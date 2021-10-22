# def z(x, y, index, cnt):
#   if index == 0:
#     print(cnt)
#     return

#   d = int(2**(index-1))

#   if (x <= r < x+d) and (y <= c < y+d):
#     z(x, y, index - 1, cnt)
#   elif (x <= r < x+d) and (y+d <= c):
#     z(x, y + d, index - 1, cnt + d*d)
#   elif (x+d <= r) and (y <= c < y+d):
#     z(x + d, y, index - 1, cnt + d*d*2)
#   elif (x+d <= r) and (y+d <= c):
#     z(x + d, y + d, index - 1, cnt + d*d*3)


# if __name__ == "__main__":
#   n, r, c = map(int, input().split())
#   z(0, 0, n, 0)






def recursion(x, y, visit_cnt, power):
  if power == 0:
    print(visit_cnt)
    return

  front = 2**(power-1)
  back = 2**(power)
  cnt = front * front

  if (x <= r < x + front) and (y <= c < y + front):  # 1사분면
    recursion(x, y, visit_cnt, power - 1)

  elif (x <= r < x + front) and (y + front <= c < y + back):  # 2사분면
    recursion(x, y + front, visit_cnt + cnt, power - 1)

  elif (x + front <= r < x + back) and (y <= c < y + front):  # 3사분면
    recursion(x + front, y, visit_cnt + cnt * 2, power - 1)

  elif (x + front <= r < x + back) and (y + front <= c < y + back):  # 4사분면
    recursion(x + front, y + front, visit_cnt + cnt * 3, power - 1)


if __name__ == "__main__":
  n, r, c = map(int, input().split())
  recursion(0, 0, 0, n)
