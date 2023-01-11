def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)


n = int(input())
ans = str(factorial(n))
cnt = 0
for i in range(len(ans)-1, -1, -1):
    if ans[i] != '0':
        print(cnt)
        break
    cnt+=1