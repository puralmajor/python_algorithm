<<<<<<< Updated upstream
from collections import deque
import sys

input = sys.stdin.readline

m, n = map(int, input().split())
miro = [list(input().rstrip()) for _ in range(n)]

visit = [[False] * m for _ in range(n)]
q = deque()
q.append((0, 0, 0))  # num_of_break_walls, x, y

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
while q:
    broken, x, y = q.popleft()
    visit[x][y] = True

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if nx == n-1 and ny == m-1:
            print(broken)
            print(sys.getsizeof(visit))
            exit()

        if 0 <= nx < n and 0 <= ny < m:
            if not visit[nx][ny]:
                if miro[nx][ny] == '0':
                    q.appendleft((broken, nx, ny))
                else:
                    q.append((broken + 1, nx, ny))
=======
n, m = map(int, input().split())
miro = [list(map(int, input().split())) for _ in range(n)]
>>>>>>> Stashed changes
