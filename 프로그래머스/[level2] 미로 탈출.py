from collections import deque


def solution(maps):
    r = len(maps)
    c = len(maps[0])
    for i in range(r):
        S = maps[i].find('S')
        if S != -1:
            s = (i, S)
            break

    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    dp = [[0]*c for _ in range(r)]
    def bfs(coo, target):
        q = deque()
        visit = set()
        q.append((*coo, 0))
        while q:
            x, y, dist = q.popleft()
            if (x, y) in visit:
                continue
            dp[x][y] = dist
            visit.add((x, y))
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < r and 0 <= ny < c and (nx, ny) not in visit and maps[nx][ny] != 'X':
                    if maps[nx][ny] != target:
                        q.append((nx, ny, dist + 1))
                    elif maps[nx][ny] == target:
                        if target == 'E':
                            return dist+1
                        else:
                            return [dist+1, (nx, ny)]
        return -1

    first = bfs(s, 'L')
    if first == -1:
        return -1
    else:
        answer, l = first

    second = bfs(l, 'E')
    if second == -1:
        return -1
    else:
        answer += second

    return answer


a = "S" + "O"*99
b = "O" * 100
c = "O" * 50 + "E" + "O" * 49
d = "X" * 19 + "L" + "X" * 80

maps = [a]

for i in range(99):
    if i == 31:
        maps.append(d)
    elif i == 78:
        maps.append(c)
    else:
        maps.append(b)

m = ["SOOOL","XXXXO","OOOOO","OXXXX","OOOOE"]
print('solution start')
print(solution(maps))
