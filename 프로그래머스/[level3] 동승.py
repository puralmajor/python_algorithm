from queue import PriorityQueue


def dijk(road, n, s):
    dist = [float('inf')] * (n + 1)
    visit = [False] * (n + 1)

    pq = PriorityQueue()
    pq.put((0, s))
    dist[s] = 0

    while pq.qsize() > 0:
        cur = pq.get()[1]
        if visit[cur]:
            continue

        visit[cur] = True

        for nx, val in road[cur]:
            if dist[nx] > dist[cur] + val:
                dist[nx] = dist[cur] + val
                pq.put((dist[nx], nx))

    return dist


def solution(n, s, a, b, fares):
    answer = 0
    road = [[] for _ in range(n + 1)]

    for start, end, val in fares:
        road[start].append((end, val))
        road[end].append((start, val))

    d1 = dijk(road, n, s)
    d2 = dijk(road, n, a)
    print(d1, d2, sep='\n')
    answer = min(d1[a] + d1[b], d1[a] + d2[b], d1[b] + d2[a])

    return answer

n = 6
s = 4
a = 6
b = 2
fares = [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]

print(solution(n,s,a,b,fares))