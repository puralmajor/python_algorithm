T = int(input())

for t in range(T):
    n, m = map(int, input().split())
    arr = [list(map(int, list(input()))) for _ in range(n)]
    a = [[-1, -1]] * n
    b = [[-1, -1]] * m

    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1:
                if a[i][0] == b[j][0] and a[i][0] != -1:
                    
