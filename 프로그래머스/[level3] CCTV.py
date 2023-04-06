def solution(routes):
    answer = 1
    routes.sort(key=lambda x: [x[1], x[0]], reverse=True)
    position = routes.pop()[1]

    while routes:
        enter, out = routes.pop()
        if position < enter:
            answer += 1
            position = out

    return answer