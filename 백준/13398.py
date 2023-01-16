n = int(input())
arr = list(map(int, input().split()))
dp = [0] * n
dp[0] = arr[0]
rec = [0, 0]

for i in range(1, n):
    if arr[i] < 0:
        if arr[i] < rec[1]:
            tmp = arr[rec[0]+1:i]
            if tmp:
                dp[i] = max(dp[i-1] + rec[1], sum(tmp), arr[i])
            else:
                dp[i] = max(dp[i-1] + rec[1], arr[i])
            rec = [i, arr[i]]

        else:
            dp[i] = max(dp[i-1] + arr[i], arr[i])

    else:
        dp[i] = max(arr[i], dp[i-1] + arr[i])
    print(dp)

print(max(dp))