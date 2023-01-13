from collections import deque
def solution(m, n, puddles):
    dx, dy = [0, 1], [1, 0]
    maps = [[0] * m for _ in range(n)]
    maps[0][0] = 1

    for x, y in puddles:
        maps[y][x] = -1

    q = deque()
    q.append((0, 0))

    visit = set()
    visit.add((0, 0))

    while True:
        x, y = q.popleft()
        if x == n - 1 and y == m - 1:
            break

        visit.add((x, y))

        for i in range(2):
            nx, ny = x + dx[i], y + dy[i]
            if nx < n and ny < m and maps[nx][ny] != -1:
                q.append((nx, ny))
                maps[nx][ny] = (maps[nx][ny]+1) % (10**9+7)

    print(*maps, sep='\n')

    return maps[-1][-1]
