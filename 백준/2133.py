n = int(input())
dp = [0] * 32
dp[0], dp[2] = 1, 3

for i in range(4, n+2, 2):
    dp[i] = dp[i-2] * 3
    for j in range(4, i, 2):
        dp[i] += 2*dp[i-j]
    dp[i] += 2

print(dp[n])