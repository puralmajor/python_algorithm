# 문제에서 주는 예시가 틀려버려서 못품
def solution(m, n, puddles):
    answer = 0
    dx, dy = [0, 1], [1, 0]
    maps = [[float('inf')] * m for _ in range(n)]
    maps[0][0] = 0
    if len(puddles) != 0:
        for p in puddles:
            maps[p[0]][p[1]] = -1

    for x in range(n):
        for y in range(m):
            if maps[x][y] == -1:
                continue

            for i in range(2):
                px, py = x + dx[i], y + dy[i]
                if n <= px or m <= py or maps[px][py] == -1:
                    continue
                maps[px][py] = min(maps[px][py], maps[x][y] + 1)

    for t in maps:
        print(t)

    return answer
