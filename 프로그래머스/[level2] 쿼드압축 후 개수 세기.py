def quard_split(arr, depth=0):
    n = len(arr)
    box = [[], [], [], []]
    for i in range(n // 2):
        box[0].append(arr[i][:n // 2])
        box[1].append(arr[i][n // 2:])
        box[2].append(arr[n // 2 + i][:n // 2])
        box[3].append(arr[n // 2 + i][n // 2:])

    for i in range(4):
        if len(set(box[i])) == 2:
            box[i] = quard_split(box[i], depth+1)
        else:
            box[i] = list(set(box[i]))

    print(box[i])
    return ''.join(box)


def solution(arr):
    answer = [0, 0]
    for i in range(len(arr)):
        arr[i] = ''.join(list(map(str,arr[i])))
    box = quard_split(arr)
    print(box)
    return answer


a = [[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]

solution(a)