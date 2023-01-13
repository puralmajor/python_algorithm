import sys
input = sys.stdin.readline

n = int(input())
wines = []

for _ in range(n):
    wines.append(int(input()))

DP = [0] * n
DP[0], DP[1] = wines[0], wines[0]+wines[1]
idx = [0, 1]

for i in range(2, n):
    print(i, DP)
    if i-1 == idx[-1] and i-2 == idx[-2]:
        cur = wines[i]
        del_idx = i
        for j in range(-2, 0):
            if wines[idx[j]] < cur:
                cur = wines[idx[j]]
                del_idx = idx[j]

        if del_idx != i:
            idx.remove(del_idx)
            idx.append(i)

        DP[i] = DP[i-1] - cur + wines[i]
    else:
        DP[i] = DP[i-1] + wines[i]
        idx.append(i)

print(DP, idx)
print(DP[-1])