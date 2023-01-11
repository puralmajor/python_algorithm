import math
from itertools import combinations
t = int(input())

for _ in range(t):
    su = list(map(int, input().split()))
    n, nums = su[0], su[1:]
    tmp = 0
    comb =combinations(nums, 2)
    for a,b in comb:
        tmp += math.gcd(a, b)

    print(tmp)