from copy import deepcopy


def move(d, r, b, depth=1):
    global answer, n, m
    if depth == 10:
        return

    print('before')
    print(r, b)

    if d == 'l':
        order = 'R' if r[1] < b[1] else 'B'
        for i in range(r[1] - 1, -1, -1):
            if (r[0], i) in blocks:
                r = [r[0], i + 1]
                break
            if [r[0], i] == out:
                r = out
                break

        for i in range(b[1] - 1, -1, -1):
            if (b[0], i) in blocks:
                b = [b[0], i + 1]
                break
            if [b[0], i] == out:
                b = out
                break

        if r == b and r != out:
            if order == 'R':
                b[1] += 1
            else:
                r[1] += 1

    if d == 'r':
        order = 'R' if r[1] > b[1] else 'B'
        for i in range(r[1] + 1, m):
            if (r[0], i) in blocks:
                r = [r[0], i - 1]
                break

            if [r[0], i] == out:
                r = out
                break

        for i in range(b[1] + 1, m):
            if (b[0], i) in blocks:
                b = [b[0], i - 1]
                break

            if [b[0], i] == out:
                b = out
                break

        if r == b and r != out:
            if order == 'R':
                b[1] -= 1
            else:
                r[1] -= 1

    if d == 'd':
        order = 'R' if r[0] > b[0] else 'B'
        for i in range(r[0] + 1, n + 1):
            if (i, r[1]) in blocks:
                r = [i - 1, r[1]]
                break

            if [i, r[1]] == out:
                r = out
                break

        for i in range(b[0] + 1, n + 1):
            if (i, b[1]) in blocks:
                b = [i - 1, b[1]]
                break

            if [i, b[1]] == out:
                b = out
                break

        if r == b and r != out:
            if order == 'R':
                b[0] -= 1
            else:
                r[0] -= 1

    if d == 'u':
        order = 'R' if r[0] < b[0] else 'B'
        for i in range(r[0] - 1, -1, -1):
            if (i, r[1]) in blocks:
                r = [i + 1, r[1]]
                break

                if [i, r[1]] == out:
                    r = out
                    break

        for i in range(b[0] - 1, -1, -1):
            if (i, b[1]) in blocks:
                b = [i + 1, b[1]]
                break

            if [i, b[1]] == out:
                b = out
                break

        if r == b and r != out:
            if order == 'R':
                b[0] += 1
            else:
                r[0] += 1

    print('after')
    print('head: ', d)
    print(r, b)
    print()
    # 공용 구간
    if r == out:
        print('occur!', out)
        if b != out:
            answer = min(answer, depth)
        return
    else:
        if d in {'u', 'd'}:
            for y in directions[:2]:
                move(y, deepcopy(r), deepcopy(b), depth + 1)
        else:
            for x in directions[2:]:
                move(x, deepcopy(r), deepcopy(b), depth + 1)


n, m = map(int, input().split())
idx_r = []
idx_b = []
out = []
blocks = set()
for i in range(m):
    cur = list(input())
    for j in range(len(cur)):
        if cur[j] == 'R':
            idx_r = [i, j]
        if cur[j] == 'B':
            idx_b = [i, j]
        if cur[j] == 'O':
            out = [i, j]
        if cur[j] == '#':
            blocks.add((i, j))

answer = 11
directions = ['l', 'r', 'd', 'u']

for i in directions:
    move(i, deepcopy(idx_r), deepcopy(idx_b))
print(answer if answer != 11 else -1)