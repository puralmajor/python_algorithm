def recursion(s, l, r, cnt = 1):
    if l >= r: return [1, cnt]
    elif s[l] != s[r]: return [0, cnt]
    else: return recursion(s, l+1, r-1, cnt+1)


def isPalindrome(s):
    return recursion(s, 0, len(s)-1)


n = int(input())

for _ in range(n):
    s = input()
    print(isPalindrome(s)[0], isPalindrome(s)[1])