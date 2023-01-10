n, m = map(int, input().split())
cards = list(map(int, input().split()))
answer = 0
for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            c_sum = cards[i] + cards[j] + cards[k]
            if c_sum > answer and c_sum <= m:
                answer = c_sum

print(answer)