def solution(s, n):
    s = list(s)
    for i in range(len(s)):
        if s[i] == ' ': continue
        start_value = ord('A') if s[i].isupper() else ord('a')
        s[i] = chr((ord(s[i]) - start_value + n) %26 + start_value)

    return ''.join(s)

s = "a B z"
n = 4
print(solution(s, n))