rows, cols = map(int, input().split())
a = [list(input()) for _ in range(rows)]
b = [list(input()) for _ in range(rows)]

change = {'1': '0', '0': '1'}
count = 0

for i in range(rows-2):
    for j in range(cols-2):
        if a[i][j] != b[i][j]:
            for k in range(3):
                a[i+k][j:j+3] = list(map(lambda x: change[x], a[i+k][j:j+3]))
            count += 1


if a == b:
    print(count)
else:
    print(-1)