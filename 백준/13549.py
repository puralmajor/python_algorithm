import sys
from queue import PriorityQueue
from collections import defaultdict

N, K = map(int, sys.stdin.readline().split())
if K <= N:
    print(N-K)
else:
    graph = defaultdict(list)
    for i in range(0, K+2):
        if 0 < i:
            graph[i].append([1, i-1])
        if i < K+1:
            graph[i].append([1, i+1])
        if 2*i <= K+1:
            graph[i].append([0, 2*i])

    def dijkstra(start, end):
        dist = [float('inf')] * (end+2)
        dist[start] = 0
        pq = PriorityQueue()
        pq.put((0, start))
        while pq.qsize() > 0:
            tmp = pq.get()
            k = tmp[0]
            u = tmp[1]
            if k > dist[u]: continue
            for w, v in graph[u]:
                if dist[v] > dist[u] + w:
                    dist[v] = dist[u] + w
                    pq.put((dist[v], v))
        return dist[end]

    print(dijkstra(N, K))