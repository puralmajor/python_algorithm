# 시간초과
def solution(stones, k):
    answer = 0
    while True:
        skip = 0
        for i in range(len(stones)):
            if stones[i] == 0:
                skip += 1
                if skip == k:
                    break
                continue

            stones[i] -= 1
            skip = 0

        if skip == k:
            break

        answer += 1

    return answer


a = [1, 2, 3, 4, 5, 6, 7, 8]
print(a[1:4])