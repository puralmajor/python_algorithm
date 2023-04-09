from heapq import heapify, heappop
from itertools import combinations

while True:
    inp = list(map(int, input().split()))
    if inp == [0]:
        break

    n = inp[0]
    inp = inp[1:]
    com = list(combinations(inp, 6))
    heapify(com)

    while com:
        print(*heappop(com))

    print()