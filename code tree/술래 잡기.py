def run():
    for r in range(m):
        if runners[r][3] <= 3:
            if runners[r][2] == 'R':
                if runners[r][1] < n - 1 and chaser != [runners[r][0], runners[r][1] + 1]:
                    runners[r][1] += 1

                elif runners[r][1] == n - 1:
                    runners[r][2] = 'L'

            if runners[r][2] == 'L':
                if runners[r][1] > 0 and chaser != [runners[r][0], runners[r][1] - 1]:
                    runners[r][1] -= 1

                elif runners[r][1] == 0:
                    runners[r][2] = 'R'
                    if chaser != [runners[r][0], 1]:
                        runners[r][1] = 1

            if runners[r][2] == 'D':
                if runners[r][0] < n - 1 and chaser != [runners[r][0] + 1, runners[r][1]]:
                    runners[r][0] += 1

                elif runners[r][0] == n - 1:
                    runners[r][2] = 'U'

            if runners[r][2] == 'U':
                if runners[r][0] > 0 and chaser != [runners[r][0] - 1, runners[r][1]]:
                    runners[r][0] -= 1

                elif runners[r][0] == 0:
                    runners[r][2] = 'R'
                    if chaser != [1, runners[r][1]]:
                        runners[r][0] = 1


def chase(turn):
    if chaser[2] == 'L':
        chaser[1] -= 1

    if chaser[2] == 'R':
        chaser[1] += 1

    if chaser[2] == 'D':
        chaser[0] += 1

    if chase[2] == 'U':
        cahser[0] -= 1


n, m, h, k = map(int, input().split())

chaser = [n // 2, n // 2, 'U']

runners = dict()

for i in range(m):
    x, y, move = map(int, input().split())
    x -= 1
    y -= 1
    distance = abs(n // 2 - x) + abs(n // 2 - y)
    runners[i] = [x, y, 'R' if move == 2 else 'D', distance]

trees = set()

for i in range(h):
    trees.add(tuple(map(int, input().split())))

score = 0

for t in range(k):
    run()
    chase(t + 1)
