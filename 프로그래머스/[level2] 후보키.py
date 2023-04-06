import pandas as pd
from itertools import combinations


def solution(relation):
    answer = 0
    relation = pd.DataFrame(relation)
    cols = relation.columns
    n = len(cols)
    usings = set()

    for i in range(1, n + 1):
        for comb in combinations(cols, i):
            temp = list(comb)
            flag = 0
            if sum(relation[temp].duplicated()) == 0:
                for j in range(1, len(temp) + 1):
                    for check in combinations(temp, j):
                        if check in usings:
                            flag = 1
                            break
                    if flag:
                        break

                if not flag:
                    answer += 1
                    usings.add(comb)

    return answer

