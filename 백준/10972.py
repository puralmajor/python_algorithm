n = int(input())
arr = list(map(int, input().split()))
rank = 1
factorial = [1, 1, 2]

for i in range(3, n+1):
    factorial.append(factorial[i-1]*i)

for i in range(n):
    order = arr[i] - (i+1)
    if order:
        rank += abs(order * factorial[n-i-1])

print(rank)