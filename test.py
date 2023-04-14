a = [1, 2, 3]
a[1:3] = list(map(lambda x: x-1, a[1:3]))
print(a)