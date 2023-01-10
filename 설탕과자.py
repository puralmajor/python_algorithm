h, w = map(int, input().split())
pan = [0 for _ in range(h)]
for i in range(h):
    pan[i] = [0 for _ in range(w)]

n = int(input())
for i in range(n):
    l, d, x, y = map(int, input().split())
    x, y = x-1, y-1
    if d == 0:
        for j in range(l):
            pan[x][y+j] = 1
    else:
        for j in range(l):
            pan[x+j][y] = 1

for i in range(h):
    for j in range(w):
        print(pan[i][j], end=' ')
    print('')
