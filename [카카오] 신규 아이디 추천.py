def solution(new_id):
    #Phase1
    id = new_id.lower()

    #Phase2
    avail = ['-', '_', '.']
    for i in id:
        if i.isalpha() or i.isdecimal() or i in avail:
            continue
        else:
            id.strip(i)

    print(id)

a = "...!@BaT#*..y.abcdefghijklm"
solution(a)