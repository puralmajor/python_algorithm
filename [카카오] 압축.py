def solution(msg):
    answer = []
    lzw = {chr(i):i-64 for i in range(65, 91)}
    idx = 27

    while msg:
        temp = 1
        while msg[:temp] in lzw.keys() and temp <= msg.__len__():
            temp += 1
        temp -= 1
        answer.append(lzw[msg[:temp]])
        lzw[msg[:temp + 1]] = idx
        idx += 1
        msg = msg[temp:]

    return answer
# 내가 풀기 실패..
# 인덱스랑 msg 자체를 수정하는 방법으로 접근했어야 하며, 인덱스를 통해서 사전검사
solution('KAKAO')
print('aaaa'[:0])