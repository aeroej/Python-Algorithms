# 원본을 유지한채, 정렬된 리스트 구하기 - sorted

# list.sort() : 원본의 순서를 변경o
# sorted(list) : 원본의 순서는 변경x, 정렬된 값만 구하기

# sort
list = [3, 2, 1]
sort = list.sort()
print('list :', list, 'sort :', sort)

# sorted
list = [3, 2, 1]
sorted = sorted(list)
print('list :', list, 'sorted :', sorted)

# -----------------------------------------------------------

# copy.copy(list) : 내부리스트는 같은 객체를 참조
# copy.deepcopy(list) : 내부리스트까지 완전한 복제

# copy
import copy

list = [1, [1, 2, 3]]
shallow = copy.copy(list)

shallow[0] = 'bug'
shallow[1].append('bug')

print(list)

# deepcopy
list = [1, [1, 2, 3]]
deep = copy.deepcopy(list)

deep[0] = 'bug'
deep[1].append('bug')

print(list)
