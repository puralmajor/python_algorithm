from itertools import permutations

n = int(input())
op = input().split()
ans1 = (0, 0, 0)
ans2 = (100, 100, 100)

for case in permutations(range(10), n+1):
    cnt = 0
    for i in range(n):
        if op[i] == '<' and case[i] < case[i+1]:
            cnt += 1
        elif op[i] == '>' and case[i] > case[i+1]:
            cnt += 1
        else:
            break

    if cnt == n:
        ans1 = max(ans1, case)
        ans2 = min(ans2, case)

print(*ans1, sep='')
print(*ans2, sep='')