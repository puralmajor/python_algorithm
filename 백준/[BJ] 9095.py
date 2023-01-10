T = int(input())

DP = [0] * 12
DP[0], DP[1], DP[2], DP[3] = 0, 1, 2, 4

for _ in range(T):
    n = int(input())
    for i in range(4, n+1):
        DP[i] = DP[i-1] + DP[i-2] + DP[i-3]
    print(DP[n])