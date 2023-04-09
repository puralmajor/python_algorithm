import sys
from collections import deque
input = sys.stdin.readline

m, n = map(int, input().split())
box = []
stack = deque()
visited = set()

for i in range(n):
    tmp = list(map(int, input().split()))
    box.append(tmp)
    for j in range(m):
        if tmp[j] == 1:
            stack.append((i, j))
            visited.add((i, j))
        if tmp[j] == -1:
            visited.add((i, j))


dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

day = 1
tomato = 0

while stack:
    x, y = stack.popleft()
    visited.add((x, y))
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if box[nx][ny] == 0:
                box[nx][ny] = box[x][y] + 1
                stack.append((nx, ny))
                day = max(day, box[nx][ny])


if len(visited) < n*m:
    print(-1)
else:
    print(day-1)