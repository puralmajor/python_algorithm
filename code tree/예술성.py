from collections import defaultdict


def rotate(arr):
    return list(map(list, zip(*arr[::-1])))


def full_rotate():
    for r in range(n//2):
        draw[n//2][r], draw[n-1-r][n//2], draw[n//2][n-1-r], draw[r][n//2] = draw[r][n//2], draw[n//2][r], draw[n-1-r][n//2], draw[n//2][n-r-1]


    arr1 = rotate(list(map(lambda x: x[:n // 2], draw[:n // 2])))
    arr2 = rotate(list(map(lambda x: x[n // 2 + 1:], draw[:n // 2])))
    arr3 = rotate(list(map(lambda x: x[:n // 2], draw[n // 2 + 1:])))
    arr4 = rotate(list(map(lambda x: x[n // 2 + 1:], draw[n // 2 + 1:])))

    for i in range(n // 2):
        draw[i][:n // 2] = arr1[i]
        draw[i][n // 2 + 1:] = arr2[i]
        draw[n // 2 + i + 1][:n // 2] = arr3[i]
        draw[n // 2 + i + 1][n // 2 + 1:] = arr4[i]




    print(*draw, sep='\n')
    print()

def dfs(x, y, group):
    if (x, y) in visit:
        return

    visit.add((x, y))
    groups[group].append((x, y))
    group_score[group] = draw[x][y]

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in visit:
            if draw[nx][ny] == draw[x][y]:
                dfs(nx, ny, group)


def cal_score(g1, g2):
    n_g1, n_g2 = len(groups[g1]), len(groups[g2])
    score_g1, score_g2 = group_score[g1], group_score[g2]
    neighbor = 0
    for x, y in groups[g1]:
        for x_, y_ in groups[g2]:
            if abs(x - x_) + abs(y - y_) == 1:
                neighbor += 1

    print(f'{g1} : {g2} score = {(n_g1 + n_g2) * score_g1 * score_g2 * neighbor}')
    return (n_g1 + n_g2) * score_g1 * score_g2 * neighbor


def total_score():
    keys = list(groups.keys())
    score = 0

    for i in range(len(keys)):
        for j in range(i + 1, len(keys)):
            temp = cal_score(keys[i], keys[j])
            score += temp

    print(score)
    return score


n = int(input())
draw = [list(map(int, input().split())) for _ in range(n)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

answer = 0

for _ in range(3):
    groups = defaultdict(list)
    group_score = defaultdict(int)
    visit = set()

    level = 0

    for i in range(n):
        for j in range(n):
            if (i, j) not in visit:
                dfs(i, j, level)
                level += 1

    print(*groups.items(), sep='\n')
    answer += total_score()
    print()
    full_rotate()

answer += total_score()

print(answer)