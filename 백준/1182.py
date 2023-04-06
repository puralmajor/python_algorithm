import sys
def dfs(cur, total):
    global answer, n
    if total == 0:
        answer += 1

    for j in range(cur+1, n):
        dfs(j, total + arr[j])


input = sys.stdin.readline
answer = 0

n, s = map(int, input().split())
arr = list(map(int, input().split()))

for i in range(n):
    dfs(i, arr[i])

print(answer)