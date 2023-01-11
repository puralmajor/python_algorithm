trans = {chr(i):i-55 for i in range(ord('A'), ord('Z')+1)}

b, n = input().split()
b, n = b[::-1], int(n)
answer = 0
for i in range(len(b)):
    tmp = b[i]
    if not tmp.isdigit():
        tmp = trans[tmp]

    answer += n**i * int(tmp)

print(answer)