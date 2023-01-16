# 타인 블로그 참고함
n = int(input())
arr = list(map(int, input().split()))
arrr = arr[::-1]

inc, dec = [1]*n, [1]*n

for i in range(n):
    for j in range(i):
        if arr[j] < arr[i]:
            inc[i] = max(inc[i], inc[j]+1)

        if arrr[j] < arrr[i]:
            dec[i] = max(dec[j] + 1, dec[i])

ans = [0] * n
for i in range(n):
    ans[i] = inc[i] + dec[n-i-1] - 1

print(max(ans))