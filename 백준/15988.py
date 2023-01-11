import sys
input = sys.stdin.readline

T = int(input())
DP = [0 for _ in range(1000001)]
DP[1], DP[2], DP[3] = 1, 2, 4
for i in range(4, 1000001):
    DP[i] = (DP[i-3] + DP[i-2] + DP[i-1])%1000000009

for _ in range(T):
    n = int(input())
    print(DP[n])