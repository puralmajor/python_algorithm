import sys
input = sys.stdin.readline

S = 0

for _ in range(int(input())):
    cmd = input().split()
    if cmd == ['all']:
        S = (1 << 21) - 1
    elif cmd == ['empty']:
        S = 0

    else:
        cmd, num = cmd[0], int(cmd[1])
        if cmd == 'add':
            S |= (1 << num)
        elif cmd == 'remove':
            S &= ~(1 << num)
        elif cmd == 'toggle':
            S ^= (1 << num)
        elif cmd == 'check':
            print(1 if S & (1 << num) != 0 else 0)
