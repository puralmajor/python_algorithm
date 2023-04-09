import sys
input = sys.stdin.readline

n = int(input())
wine = []
for _ in range(n):
    wine.append(int(input()))

if n < 4:
    print(sum(wine))
else:
    DP = [0] * n
    DP[0] = wine[0]
    DP[1] = DP[0] + wine[1]
    idx = [0, 1]

    for i in range(2, n):
        print(i, DP, sep='\n')
        if i-1 == idx[-1] and i-2 == idx[-2]:
            comp = wine[i]
            del_idx = i
            for j in range(len(idx)):
                if wine[idx[j]] < comp:
                    comp = wine[idx[j]]
                    del_idx = idx[j]

            if i != del_idx:
                idx.remove(del_idx)
                idx.append(i)

            DP[i] = DP[i-1] - comp + wine[i]

        else:
            idx.append(i)
            DP[i] = DP[i-1] + wine[i]



    print(DP[-1])