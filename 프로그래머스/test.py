a = "S" + "O"*99
b = "O" * 100
c = "O" * 50 + "E" + "O" * 49
d = "X" * 19 + "L" + "X" * 80

maps = [a]

for i in range(99):
    if i == 31:
        maps.append(d)
    elif i == 78:
        maps.append(c)
    else:
        maps.append(b)

print(*maps, sep='\n')