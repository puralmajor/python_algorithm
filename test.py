import sys
import itertools
from collections import deque

sys.setrecursionlimit(10**6)
def bfs(x, y, lv):
    q = deque()
    q.append((x, y))
    visited.add((x, y))
    maps[x][y] = lv
    end_points = set()

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if maps[nx][ny] == 1 and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    maps[nx][ny] = lv
                    q.append((nx, ny))

                elif maps[nx][ny] == 0:
                    end_points.add((x, y))

    check_point.append(end_points)


n = int(input())
maps = [list(map(int, input().split())) for _ in range(n)]
level = 2
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
check_point = []
visited = set()

for i in range(n):
    for j in range(n):
        if maps[i][j] == 1:
            bfs(i, j, level)
            level += 1

answer = float('inf')

for i in range(len(check_point)):
    for x, y in check_point[i]:
        for _x, _y in itertools.chain(*check_point[i+1:]):
            answer = min(abs(x-_x) + abs(y-_y)-1, answer)

print(answer)
