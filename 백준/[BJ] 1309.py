import sys

n = int(sys.stdin.readline())
if n == 0:
    print(1)
elif n == 1:
    print(3)
else:
    DP = [0] * (n+1)
    DP[1], DP[2] = 3, 7

    for i in range(3, n+1):
        DP[i] = (DP[i-2] + DP[i-1]*2) % 9901

    print(DP[n])