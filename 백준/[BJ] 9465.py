import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n = int(input())
    stickers = [list(map(int, input().split())) for _ in range(2)]
    if n == 1:
        print(max(stickers[0][0], stickers[1][0]))
        continue

    stickers[0][1] += stickers[1][0]
    stickers[1][1] += stickers[0][0]

    for j in range(2, n):
        for i in range(2):
            stickers[i][j] += max(stickers[i-1][j-1], stickers[i-1][j-2])

    print(max(stickers[0][-1], stickers[1][-1]))