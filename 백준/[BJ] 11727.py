n = int(input())
DP = [0] * (n+1)
DP[0], DP[1], DP[2] = 0, 1, 3
for i in range(3, n+1):
    DP[i] = (2*DP[i-2] + DP[i-1]) % 10007

print(DP[n])