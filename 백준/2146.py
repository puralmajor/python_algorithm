import sys
from collections import deque
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def dfs(x, y, lv):

    maps[x][y] = lv

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if maps[nx][ny] == 1:
                dfs(nx, ny, lv)
            elif maps[nx][ny] == 0:
                end_point.append((x, y))


def bfs(x, y):
    global answer
    q = deque()
    q.append((x, y, 0))
    visit = [[False]*n for _ in range(n)]

    while q:
        cur_x, cur_y, dist = q.popleft()
        visit[cur_x][cur_y] = True

        for i in range(4):
            nx, ny = cur_x + dx[i], cur_y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visit[nx][ny]:
                if maps[nx][ny] == 0:
                    q.append((nx, ny, dist+1))
                elif maps[nx][ny] != maps[x][y]:
                    answer = min(abs(x-nx) + abs(y-ny) - 1, answer)
                    del visit
                    return


answer = 10**7
n = int(input())
maps = [list(map(int, input().split())) for _ in range(n)]
level = 2
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
print(sys.getsizeof(maps))
for i in range(n):
    for j in range(n):
        if maps[i][j] == 1:
            end_point = []
            dfs(i, j, level)
            level += 1

            for x, y in end_point:
                bfs(x, y)


print(answer)
