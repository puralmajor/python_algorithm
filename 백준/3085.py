def candy_count(x, y):
    global n
    ea_x, ea_y = 1, 1
    cur = candy[x][y]

    for ny in range(y+1, n):
        if candy[x][ny] == cur:
            ea_y += 1
        else:
            break

    for py in range(y-1, -1, -1):
        if candy[x][py] == cur:
            ea_y += 1
        else:
            break

    for nx in range(x+1, n):
        if candy[nx][y] == cur:
            ea_x += 1
        else:
            break

    for px in range(x-1, -1, -1):
        if candy[px][y] == cur:
            ea_x += 1
        else:
            break

    return max(ea_x, ea_y)



n = int(input())
candy = [list(input()) for _ in range(n)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
ans = 0

for x in range(n):
    for y in range(n):
        ans = max(ans, candy_count(x,y))
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if (0 <= nx < n) and (0 <= ny < n) and candy[x][y] != candy[nx][ny]:
                candy[x][y], candy[nx][ny] = candy[nx][ny], candy[x][y]
                ans = max(ans, candy_count(x, y))
                candy[x][y], candy[nx][ny] = candy[nx][ny], candy[x][y]

print(ans)