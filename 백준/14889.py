from itertools import combinations

n = int(input())
stat = [list(map(int, input().split())) for _ in range(n)]
diff = 10**6

for i in combinations(range(n), n//2):
    people = list(set(range(n)) - set(i))
    s = 0
    l = 0
    for j in combinations(i, 2):
        s += stat[j[0]][j[1]] + stat[j[1]][j[0]]

    for k in combinations(people, 2):
        l += stat[k[0]][k[1]] + stat[k[1]][k[0]]

    diff = min(diff, abs(l-s))

print(diff)