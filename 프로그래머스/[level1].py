s = "2three45sixseven"

stoi = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

for i in stoi:
    if i in s:
        s = s.replace(i, str(stoi.index(i)))

print(s)