n = int(input())
price = [0]
price.extend(list(map(int, input().split())))
DP = [0] * (n+1)
for i in range(1, n+1):
    