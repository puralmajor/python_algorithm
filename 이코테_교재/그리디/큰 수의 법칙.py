n, m, k = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
repeat = arr[-1] * (k-1) + arr[-2]
ans = repeat * (m//k) + arr[-1] * (m%k)

print(ans)