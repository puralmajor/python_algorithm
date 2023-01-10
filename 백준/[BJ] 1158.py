from collections import deque
n, k = map(int, input().split())
arr = deque([i for i in range(1, n+1)])
pus = []
cnt = 0
while arr:
    if cnt == k-1:
        pus.append(arr.popleft())
        cnt = 0
    else:
        arr.append(arr.popleft())
        cnt += 1

print("<"+str(pus)[1:-1]+">")