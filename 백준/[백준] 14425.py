n, m = map(int, input().split())

first = []
cnt = 0
for _ in range(n):
    first.append(input())

first = set(first)

for _ in range(m):
    temp = input()
    if temp in first:
        cnt += 1

print(cnt)