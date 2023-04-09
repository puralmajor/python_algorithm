def nm10(idx, depth, temp):
    global n
    global m
    if depth == m-1:
        ans.append(temp)
        return

    for j in range(idx+1, n):
        nm10(j, depth+1, temp+[arr[j]])


n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
ans = []

for i in range(n):
    nm10(i, 0, [arr[i]])

for i in sorted(list(set(map(tuple, ans)))):
    print(*i)