def nm11(idx, depth, temp):
    global n
    global m
    if depth == m-1:
        ans.append(temp)
        return

    for j in range(n):
        nm11(idx, depth+1, temp+[arr[j]])


n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
ans = []

for i in range(n):
    nm11(i, 0, [arr[i]])

for a in sorted(list(set(map(tuple, ans)))):
    print(*a)