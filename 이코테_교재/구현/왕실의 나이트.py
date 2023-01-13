place = list(input())
place[0], place[1] = ord(place[0]) - 96, int(place[1])

case = [[-2, -1], [-2, 1], [-1, -2], [-1, 2], [2, -1], [2, 1], [1, -2], [1, 2]]
cnt = 0

for dx, dy in case:
    x = place[0] + dx
    y = place[1] + dy
    if 0 < x < 9 and 0 < y < 9:
        cnt += 1

print(cnt)