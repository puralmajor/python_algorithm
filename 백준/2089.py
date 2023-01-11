n = int(input()) * (-1)
binary = '' if n != 0 else '0'
while n:
    binary += str(abs(n%(-2)))
    n = n//(-2)

print(binary[::-1])