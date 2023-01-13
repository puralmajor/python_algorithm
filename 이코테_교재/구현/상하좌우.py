n = int(input())
move = list(input().split())
cur = [1, 1]
moving = {'R': 1 , 'L ': -1, 'U': -1, 'D': 1}

for i in move:
    if i == 'U' or i == 'D':
        cur[0] += moving[i]
        if cur[0] == 0:
            cur[0] += 1
        elif cur[0] == n+1:
            cur[0] -= 1
    else:
        cur[1] += moving[i]
        if cur[1] == 0:
            cur[1] += 1
        elif cur[1] == n+1:
            cur[1] -= 1

print(*cur)

