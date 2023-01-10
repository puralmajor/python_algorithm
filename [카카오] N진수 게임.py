def solution(n, t, m, p):
    answer = ''
    for i in range(p,t*m, m):
        if i == t*i+p:
            answer = i%n

    print(answer)
    return answer

solution(2,4,2,1)

4*2 + 1
0 1 1 0 1 1 1 0 0 1 0 1 1 1 0 1 1 1
8번