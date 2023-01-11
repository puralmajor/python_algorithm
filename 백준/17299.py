from collections import Counter

n = int(input())
a = list(map(int, input().split()))
c = Counter(a)
stack = []
answer = [-1] * n

for i in range(n):
    while stack and c[a[stack[-1]]] < c[a[i]]:
        answer[stack.pop()] = a[i]
    stack.append(i)

print(*answer)