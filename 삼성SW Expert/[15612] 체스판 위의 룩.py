T = int(input())

for t in range(T):
    attack = [False] * 8
    looks = 0
    column = False
    for i in range(8):
        temp = list(input())
        row = False

        for j in range(8):
            if temp[j] == 'O':
                if row or attack[j]:
                    column = True
                    break

                looks += 1
                flag = True
                attack[j] = True

        if column:
            break

    if column or looks != 8:
        print(f"#{i + 1} no")
    else:
        print(f"#{i + 1} yes")