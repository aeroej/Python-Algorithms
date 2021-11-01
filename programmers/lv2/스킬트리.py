# Summer/Winter Coding(~2018)

import re

def solution(skill, skill_trees):
    res = len(skill_trees)

    for skill_tree in skill_trees:
        skill_tree = re.sub('[^{0}]'.format(skill), '', skill_tree)

        for i in range(len(skill_tree)):
            if skill[i] != skill_tree[i]:
                res -= 1
                break

    return res
