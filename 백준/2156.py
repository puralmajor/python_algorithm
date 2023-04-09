import sys
input = sys.stdin.readline

n = int(input())
wines = []

for _ in range(n):
    wines.append(int(input()))

dp = [0] * n
if n == 1:
    print(wines[0])
    exit()

dp[0], dp[1] = wines[0], wines[0]+wines[1]

for i in range(2, n):
    dp[i] = max(dp[i-1], dp[i-2] + wines[i], dp[i-3] + wines[i-1] + wines[i])

print(max(dp))