def solution(record):
    answer = []
    id_nic = {}

    for j in record:
        i = j.split(' ')
        cmd = i[0]
        if cmd == 'Enter':
            id_nic[i[1]] = i[2]
            answer.append(i[1] + '님이 들어왔습니다.')
        elif cmd == 'Leave':
            answer.append(i[1] + '님이 나갔습니다.')
        elif cmd == 'Change':
            id_nic[i[1]] = i[2]

    tmp = []
    for i in answer:
        j = i.split('님이')
        j[0] = id_nic[j[0]] +'님이'
        tmp.append(''.join(j))

    return tmp
