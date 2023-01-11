n = int(input())
price = [0]

price.extend(list(map(int, input().split())))

for i in range(2, n+1):
    for j in range(i//2, i):
        price[i] = min(price[j]+price[i-j], price[i])

print(price[n])