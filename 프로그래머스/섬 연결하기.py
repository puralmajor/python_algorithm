from queue import PriorityQueue
# 다익스트라 x
def solution(n, costs):
    answer = 0
    island = [[] for _ in range(n)]

    for e1, e2, w in costs:
        island[e1].append((e2, w))
        island[e2].append((e1, w))

    visited = [False] * (n+1)
    dist = [float('inf')] * (n+1)
    q = PriorityQueue()
    q.put((0, 0)) # 최단거리, 노드번호
    dist[0] = 0
    bridge = [0] * (n+1)
    while q.qsize()>0:
        cur_node = q.get()[1]
        if visited[cur_node]: continue

        visited[cur_node] = True

        for nx, val in island[cur_node]:
            if dist[nx] > dist[cur_node] + val:
                dist[nx] = dist[cur_node] + val
                bridge[nx] = val
                q.put((dist[nx], nx))

    print(dist)
    print(bridge)


solution(6, [[0, 1, 1], [0, 3, 3], [1, 2, 2], [1, 5, 2], [2, 3, 4], [2, 4, 5], [3, 5, 1], [4, 5, 1]])

