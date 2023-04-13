from collections import Counter
n, t, p = map(int, input().split())
if n != 0:
    ranking = list(map(int, input().split()))
if n == 0:
    print(1)
elif n == p and ranking[-1] >= t:
    print(-1)
elif n < p and ranking[-1] > t:
    print(n+1)
elif n < p and ranking[-1] == t:
    print(ranking.index(ranking[-1])+1)
else:
    rank = 1
    count = Counter(ranking)
    while ranking[rank-1] > t:
        rank += count[ranking[rank-1]]
    print(rank)