n = int(input())
arr = list(map(int, input().split()))[-1::-1]
dp = [1] * n

for i in range(1, n):
    for j in range(i):
        if arr[j] < arr[i] and dp[i] < dp[j] + 1:
            dp[i] = dp[j]+1

print(max(dp))