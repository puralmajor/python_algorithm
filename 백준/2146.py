import sys
import itertools


sys.setrecursionlimit(10**6)
def dfs(x, y, lv):
    if (x, y) in visited:
        return

    visited.add((x, y))
    maps[x][y] = lv

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if maps[nx][ny] != 0 and (nx, ny) not in visited:
                dfs(nx, ny, lv)
            elif maps[nx][ny] == 0:
                end_point.add((x, y))


n = int(input())
maps = [list(map(int, input().split())) for _ in range(n)]
level = 2
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
check_point = []
visited = set()
for i in range(n):
    for j in range(n):
        if maps[i][j] == 1:
            end_point = set()
            dfs(i, j, level)
            level += 1
            check_point.append(end_point)

answer = float('inf')

for i in range(len(check_point)):
    for x, y in check_point[i]:
        for _x, _y in itertools.chain(*check_point[i+1:]):
            answer = min(abs(x-_x) + abs(y-_y)-1, answer)

print(answer)
