import itertools

a = [1, 2, 3]

# combinations 조합(s)
# output: [(1, 2), (1, 3), (2, 3)] --> iterable의 정렬순서를 유지함 --> dfs에서 depth 쓸 때
print(list(itertools.combinations(a, 2)))


# permutations 순열(sp) 
# output : [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)] --> iterable의 정렬순서는 고려하지 않는 모든 경우의 수 --> dfs에서 for문과 visited 쓸 때
print(list(itertools.permutations(a, 2)))
# output : [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]
print(list(itertools.permutations(a)))


# product 중복순열(p) 
# output : [(1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (3, 3)] --> 순열에서 (1, 1)도 포함할 때 --> dfs에서 for문만 쓸 때
print(list(itertools.product(a, a)))

# Python itertools 공식문서 https://docs.python.org/3/library/itertools.html
