from collections import deque

n, m = map(int, input().split())
miro = [list(map(int, list(input()))) for _ in range(n)]

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
q = deque()
q.append((0, 0))
visit = set((0, 0))

while q:
    x, y = q.popleft()
    if x == n-1 and y == m-1:
        break

    visit.add((x, y))
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if not (-1 < nx < n and -1 < ny < m):
            continue

        if miro[nx][ny] != 0:
            q.append((nx, ny))
            if (nx, ny) not in visit:
                miro[nx][ny] = miro[x][y] + 1

print(miro[x-1][y-1])