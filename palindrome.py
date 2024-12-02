def isPalindrom(strs):
    while len(strs) > 1:
        if strs.pop(0) != strs.pop():
            return False
        return True

strs = "EOE"
strs = list(strs)
if isPalindrom(strs):
    print("is Palindrom")
else:
    print("not Palindrom")