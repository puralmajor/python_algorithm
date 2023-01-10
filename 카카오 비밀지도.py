def decode(l, n):
    dec = format(n, 'b')
    dec = '0'*(l-len(dec)) + dec
    return dec

arr1 = [9, 20, 28, 18, 11]
arr2 = [30, 1, 21, 17, 28]

map1 = [0 for _ in range(5)]
map2 = [0 for _ in range(5)]

for i in range(5):
    map1[i] = list(decode(5, arr1[i]))
    map2[i] = list(decode(5, arr2[i]))

for i in range(5):
    for j in range(5):
        if map1[i][j] == '1' or map2[i][j] == '1':
            map2[i][j] = '#'
        else:
            map2[i][j] = ' '
    map2[i] = ''.join(map2[i])


print(map2)