def solution(n, results):
    answer = 0
    rank = {i + 1: [set(), set()] for i in range(n)}
    order = [0] * (n + 1)

    for win, lose in results:
        rank[win][0].add(lose)
        rank[lose][1].add(win)

    for _ in range(2):
        for i in rank.keys():
            for wins in rank[i][0]:
                rank[i][0] = rank[i][0].union(rank[wins][0])

            for loses in rank[i][1]:
                rank[i][1] = rank[i][1].union(rank[loses][1])

    for i in rank.keys():
        if len(rank[i][0]) + len(rank[i][1]) == n - 1:
            answer += 1

    return answer