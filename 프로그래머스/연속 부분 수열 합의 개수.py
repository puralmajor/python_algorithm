def solution(elements):
    answer = set()
    n = len(elements)

    for i in range(1, n + 1):
        for _ in range(n):
            print(elements)
            print(elements[:i])
            answer.add(sum(elements[:i]))
            for _ in range(i):
                elements.append(elements.pop(0))

    return len(answer)


print(solution([7,4,1,1,9]))