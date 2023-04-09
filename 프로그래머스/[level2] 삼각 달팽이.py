def solution(n):
    answer = [[0] * i for i in range(1, n + 1)]
    dx = 0
    x, y = 0, 0
    cur = 1
    while n:
        if dx == 0:
            for i in range(n):
                answer[x][y] = cur
                cur += 1
                x += 1
            x, y = x - 1, y + 1
            dx = 1

        elif dx == 1:
            for i in range(n):
                answer[x][y] = cur
                cur += 1
                y += 1
            y -= 1
            dx = 2

        else:
            for i in range(n):
                x, y = x - 1, y - 1
                answer[x][y] = cur
                cur += 1
            x += 1
            dx = 0

        n -= 1

    ans = []
    for i in answer:
        ans.extend(i)

    return ans