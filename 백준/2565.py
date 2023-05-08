def crossing_count():
    cross = [0] * (n+1)
    for i in a.keys():
        for j in range(1, a[i]):
            if b[j] < i:
                cross[i] += 1

    return cross


n = int(input())
lines = [list(map(int, input().split())) for _ in range(n)]
a = dict(sorted(lines))
b = dict(sorted(lines, key=lambda x: x[1]))

print(a)
print(b)
cross = crossing_count()
print(cross)