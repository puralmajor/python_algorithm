from collections import Counter
s = input()
cnt = [0]*26
c = Counter(s)

for k in c.keys():
    cnt[ord(k)-97] = c[k]

print(*cnt)