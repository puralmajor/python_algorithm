n, m = map(int, input().split())
char = list(map(int, input().split()))
maps = [list(map(int, input().split())) for _ in range(n)]
cnt = 1
moves = {0: [-1, 0], 1: [0, 1], 2:[1, 0], 3:[0, -1]}
stop_cnt = 0
while True:
    # x = column, y = row
    x, y = char[0], char[1]
    maps[x][y] = 1
    char[2] -= 1

    if char[2] < 0:
        char[2] = 3
        stop_cnt += 1

    move = moves[char[2]]
    nx, ny = x+move[1], y+move[0]

    if maps[nx][ny] != 1:
        char[:2] = [nx, ny]
        stop_cnt = 0
        cnt += 1

    if stop_cnt == 4:
        break

print(cnt)
