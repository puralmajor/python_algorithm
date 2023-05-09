T = int(input())
M = 10**9
dp = [False] * M
for i in range(2, int(M**.5)+1):
    if dp[i] is False:
        for j in range(i+i, M, i):
            dp[j] = True

for t in range(T):
    n = int(input())
    x = 4