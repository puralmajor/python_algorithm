n, m = map(int, input().split())
cards = [list(map(int, input().split())) for _ in range(n)]
ans = 0

for i in range(n):
    if ans < min(cards[i]):
        ans = min(cards[i])

print(ans)