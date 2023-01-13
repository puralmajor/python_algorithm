n, m = map(int, input().split())
ice = [list(map(int, list(input()))) for _ in range(n)]
print(*ice, sep='\n')
cnt = 0

def dfs(x, y):
    if ice[x][y] == 1:
        return

    ice[x][y] = 1
    dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if -1 < nx < n and -1 < ny < m:
            dfs(nx, ny)

for i in range(n):
    for j in range(m):
        if ice[i][j] == 0:
            dfs(i, j)
            cnt += 1

print(cnt)