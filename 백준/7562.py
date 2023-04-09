from collections import deque
t = int(input())

for _ in range(t):
    n = int(input())
    a, b = map(int, input().split())
    target = tuple(map(int, input().split()))
    chess = [[0] * n for _ in range(n)]
    chess[a][b] = 1
    if (a, b) == target:
        print(0)
        continue

    q = deque()
    q.append((a, b))
    move = ((1, 2), (1, -2), (2, 1), (2, -1), (-1, -2), (-1, 2), (-2, -1), (-2, 1))
    flag = True
    while q and flag:
        x, y = q.popleft()
        for dx, dy in move:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and chess[nx][ny] == 0:
                if (nx, ny) == target:
                    print(chess[x][y])
                    flag = False
                    break

                chess[nx][ny] = chess[x][y] + 1
                q.append((nx, ny))