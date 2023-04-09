def dfs(x, y):
    global w, h
    if (x, y) in visited:
        return

    visited.add((x, y))

    for i in range(8):
        nx, ny = x+dx[i], y+dy[i]
        if 0 <= nx < h and 0 <= ny < w and maps[nx][ny]:
            dfs(nx, ny)

while True:
    w, h = map(int, input().split())

    if w == h == 0:
        break

    maps = [list(map(int, input().split())) for _ in range(h)]
    visited = set()
    dx, dy = [-1, 1, 0, 0, -1, 1, -1, 1], [0, 0, -1, 1, -1, 1, 1, -1]
    cnt = 0
    for i in range(h):
        for j in range(w):
            if maps[i][j] and (i, j) not in visited:
                dfs(i, j)
                cnt += 1

    print(cnt)

