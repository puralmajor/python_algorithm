miro = [0 for _ in range(10)]
for i in range(10):
    miro[i] = list(map(int, input().split()))

x, y = 1, 1


while y != 10 and x != 10:
    if miro[x][y] == 2:
        miro[x][y] = 9
        break

    if miro[x][y] == 1:
        y -= 1
        x += 1
    else:
        miro[x][y] = 9
        y += 1

for i in range(10):
    for j in range(10):
        print(miro[i][j], end=' ')
    print('')