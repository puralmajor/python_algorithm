from itertools import combinations
from heapq import heapify, heappop
l, c = map(int, input().split())
arr = input().split()
ja, mo = [], []
answer = set()

for i in sorted(arr):
    if i in {'a', 'e', 'i', 'o', 'u'}:
        mo.append(i)
    else:
        ja.append(i)

for i in range(len(mo)):
    for j in range(len(ja)):
        for k in range(j+1, len(ja)):
            remain = mo[i+1:] + ja[:j] + ja[k+1:]
            for t in sorted(combinations(remain, l-3)):
                temp = mo[i] + ja[j] + ja[k] + ''.join(t)
                temp = ''.join(sorted(temp))
                answer.add(temp)

answer = list(answer)
heapify(answer)

while answer:
    print(heappop(answer))
