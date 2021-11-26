from itertools import combinations

def solution(relation):
    keys = []  # 후보키
    t = len(relation)  # 튜플 수
    c = len(relation[0])  # 컬럼 수
    c_idx = [_ for _ in range(c)]  # [0, 1, 2, ...]

    for i in range(1, c + 1):
        # 컬럼의 집합
        # (학번), (이름), ..., (학번, 이름), (학번, 전공), ..., (학번, 이름, 전공), ...
        for combi in combinations(c_idx, i):
            # 최소성
            flag = False
            for key in keys:
                if len(set(key + combi)) == len(combi):
                    flag = True
                    break

            if flag:
                continue

            # 유일성
            tuples = set()
            for re in relation:
                tuples.add(tuple([re[idx] for idx in combi]))

            if len(tuples) == t:
                keys.append(combi)

    return len(keys)
