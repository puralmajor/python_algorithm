n, m = map(int, input().split())

듣잡 = set()
for _ in range(n):
    듣잡.add(input())

보잡 = set()
for _ in range(m):
    보잡.add(input())

ans = []
for i in 듣잡:
    if i in 보잡:
        ans.append(i)

ans = sorted(ans)
print(len(ans))
for i in ans:
    print(i)