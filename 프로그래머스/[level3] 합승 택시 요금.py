def solution(n, s, a, b, fares):
    answer = float('inf')
    cost = [[float('inf')] * (n+1) for _ in range(n+1)]

    # cost 중에서 fares에서 제시된 도로
    for u, v, _cost in fares:
        cost[u][v] = _cost
        cost[v][u] = _cost

    #플로이드 와샬 알고리즘
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                if i == j:
                    cost[i][j] = 0
                else:
                    cost[i][j] = min(cost[i][j], cost[i][k] + cost[k][j])


    for i in range(1, n+1):
        answer = min(cost[s][i] + cost[i][a] + cost[i][b], answer)

    return answer