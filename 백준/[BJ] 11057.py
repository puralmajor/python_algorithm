n = int(input())
DP = [1] * 10
for i in range(n-1):
    for j in range(10):
        DP[j] = sum(DP[j:])

print(sum(DP)%10007)