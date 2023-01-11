import math
from itertools import combinations

n, s = map(int, input().split())
arr = list(map(lambda x: abs(int(x)-s), input().split()))
gcd = arr.pop()
while arr:
    a = arr.pop()
    gcd = math.gcd(gcd, a)
print(gcd)