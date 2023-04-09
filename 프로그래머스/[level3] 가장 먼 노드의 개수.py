from queue import PriorityQueue


def solution(n, edge):
    answer = 0
    vtx = [[] for _ in range(n)]
    target = 0
    for u, v in edge:
        vtx[u - 1].append(v - 1)
        vtx[v - 1].append(u - 1)

    dist = [float('inf')] * n
    dist[0] = 0

    pq = PriorityQueue()
    pq.put((0, 0))

    while pq.qsize() > 0:
        _, cur = pq.get()

        for nx in vtx[cur]:
            if dist[cur] + 1 < dist[nx]:
                dist[nx] = dist[cur] + 1
                target = max(dist[nx], target)
                pq.put((dist[nx], nx))

    for i in dist:
        if i == target:
            answer += 1

    return answer