n = int(input())
sg = list(map(int, input().split()))
find = dict()

for i in sg:
    if i in find:
        find[i] += 1
    else:
        find[i] = 1

m = int(input())
search = list(map(int, input().split()))

for i in search:
    if i in find:
        print(find[i], end=' ')
    else:
        print(0, end=' ')