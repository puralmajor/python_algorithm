n = int(input())
candy = [list(map(int, input().split()))]
dx, dy = [1, 0], [0, 1]

for x in range(n):
    cnt = 1
    for y in range(1, n-1):
        if candy[x][y-1] != candy[x][y]:
            for i in range(2):
                nx, ny = x+dx[i], y+dy[i]
        else:
            cnt += 1