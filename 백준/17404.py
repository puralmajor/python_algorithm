import sys
inp = sys.stdin.readline

n = int(inp())
houses = [list(map(int, inp().split())) for _ in range(n)]

houses[1][0] += min(houses[0][1], houses[0][2])
houses[1][1] += min(houses[0][0], houses[0][2])
houses[1][2] += min(houses[0][1], houses[0][0])

cases = [[houses[0].index(min(houses[0][1], houses[0][2]))],
         [houses[0].index(min(houses[0][0], houses[0][2]))],
         [houses[0].index(min(houses[0][1], houses[0][0]))]]

for i in range(2, n):
    houses[i][0] += min(houses[i-1][1], houses[i-1][2])
    cases[0].append(houses[i-1].index(min(houses[i-1][1], houses[i-1][2])))

    houses[i][1] += min(houses[i-1][0], houses[i-1][2])
    cases[1].append(houses[i-1].index(min(houses[i-1][0], houses[i-1][2])))

    houses[i][2] += min(houses[i-1][1], houses[i-1][0])
    cases[2].append(houses[i-1].index(min(houses[i-1][1], houses[i-1][0])))

print(cases)
print(houses)