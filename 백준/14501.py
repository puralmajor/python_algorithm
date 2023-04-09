n = int(input())
rsv = []
for _ in range(n):
    rsv.append(list(map(int, input().split())))

dp = [0] * n

for i, v in enumerate(rsv):
    day, gain = v
    if dp[i] == 0:
        dp[i:i+day] = [gain] * day