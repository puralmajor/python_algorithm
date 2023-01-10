import sys
from collections import deque
input = sys.stdin.readline

n, max_k = map(int, input().split())
items = []
ans = 0
for _ in range(n):
    items.append(list(map(int, input().split())))

bag = deque()
weight = deque()
for w, v in items:
    bag.append(v)
    weight.append(w)
    if max_k < sum(weight):
        while max_k < sum(weight)


