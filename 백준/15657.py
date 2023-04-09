def nm8(idx, depth, temp):
    global n
    global m
    if depth == m-1:
        print(*temp)
        return

    for j in range(idx, n):
        nm8(j, depth+1, temp+[arr[j]])


n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()


for i in range(n):
    nm8(i, 0, [arr[i]])
