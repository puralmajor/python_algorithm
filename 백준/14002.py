import sys

input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))
DP = [[i] for i in A]

for i in range(n):
    for j in range(i):
        if DP[j][-1] < A[i]:
            DP[j].append(A[i])

print(max(map(len, DP)))
print(*max(DP, key=len))
