import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n = int(input())
    stickers = [list(map(int, input().split())) for _ in range(2)]
    # 이 코드는 n-1을 건너뛸 때 계산할 수 없다.
    if n % 2 != 0:
        for i in range(2, n, 2):
            stickers[0][i] += max(stickers[1][i-1]+stickers[0][i-2], stickers[1][i-2])
            stickers[1][i] += max(stickers[0][i-1]+stickers[1][i-2], stickers[0][i-2])
    else:
        stickers[0][1] += stickers[1][0]
        stickers[1][1] += stickers[0][0]
        for i in range(3, n, 2):
            stickers[0][i] += max(stickers[1][i-1]+stickers[0][i-2], stickers[1][i-2])
            stickers[1][i] += max(stickers[0][i-1]+stickers[1][i-2], stickers[0][i-2])

    print(max(stickers[0][n-1], stickers[1][n-1]))