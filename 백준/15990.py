T = int(input())

DP = [0] * 100001
DP[1], DP[2], DP[3], DP[4], DP[5] = 1, 1, 3, 3, 4, 
for _ in range(T):
    n = int(input())