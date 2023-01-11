import sys
sys.setrecursionlimit(10**10)

def factorial(n):
    if n == 1 or n == 0:
        return 1
    return n * factorial(n-1)

n, m = map(int, input().split())
p, q = 1, factorial((n-m))
for i in range(m+1, n+1):
    p *= i

ans = p//q
cnt = 0
while True:
    if ans%10 != 0:
        print(cnt)
        break
    ans, cnt = ans//10, cnt+1
