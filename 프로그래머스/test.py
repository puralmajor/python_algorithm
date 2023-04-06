temp = []
visit = [1, 2]

for _ in range(3):
    temp.append(visit)

for i in range(3):
    x = temp.pop()
    x.append(i)