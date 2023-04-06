n = int(input())
m = int(input())
broken = set(input().split())
avail = {i for i in range(10) if str(i) not in broken}
cur = ''
up, down = n, n

if n == 100:
    print(0)
    exit()

for i in str(n):
    if i in broken:
        break
    else:
       cur += i

print(cur)