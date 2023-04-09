def solution(sequence):
    answer = 0
    n = len(sequence)

    for i in range(n):
        for j in range(i + 1, n):
            a = [(-1) ** k for k in range(j - i)]
            b = [(-1) ** (k + 1) for k in range(j - i)]
            answer = max(sum(map(lambda x: x[0] * x[1], zip(a, answer[i:j]))), answer)
            answer = max(answer, sum(map(lambda x: x[0] * x[1], zip(b, answer[i:j]))))

    return answer