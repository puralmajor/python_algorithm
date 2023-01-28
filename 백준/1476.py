target = list(map(int, input().split()))
start = [1, 1, 1]
year = 1

while start != target:
    start[0] = start[0]+1 if start[0] < 15 else 1
    start[1] = start[1]+1 if start[1] < 28 else 1
    start[2] = start[2]+1 if start[2] < 19 else 1
    year += 1

print(year)