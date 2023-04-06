from collections import deque
def solution(maps):
    answer = []
    r, c = len(maps), len(maps[0])
    maps = list(map(list, maps))
    visit = [[0] * c for _ in range(r)]
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

    def bfs(x, y):
        if visit[x][y] or maps[x][y] == 'X':
            return

        q = deque()
        q.append((x, y))
        visit[x][y] = 1
        val = 0
        while q:
            cx, cy = q.popleft()
            val += int(maps[cx][cy])

            for i in range(4):
                nx, ny = cx+dx[i], cy+dy[i]
                if 0 <= nx < r and 0 <= ny < c and not visit[nx][ny] and maps[nx][ny] != 'X':
                    q.append((nx, ny))
                    visit[nx][ny] = 1

        return val

    for i in range(r):
        for j in range(c):
            if maps[i][j] != 'X':
                life = bfs(i, j)
                if life:
                    answer.append(life)

    if answer:
        answer.sort()
        return answer
    else:
        return [-1]