from collections import deque

n, m = map(int, input().split())
miro = [list(map(int, list(input()))) for _ in range(n)]

q = deque()
visit = [[0] * m for _ in range(n)]
q.append((0, 0, 1))
answer = 1

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

while q:
    x, y, step = q.popleft()
    if visit[x][y] != 0:
        continue
    visit[x][y] = step

    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0 <= nx < n and 0 <= ny < m and miro[nx][ny]:
            q.append((nx, ny, step+1))

print(visit[n-1][m-1])