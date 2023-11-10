import math


def getTime(s: str) -> int:
    res, cur = 0, 0
    for i in range(len(s)):
        index = ord(s[i]) - 65
        clw = abs(cur - index)
        aclw = 26 - clw
        res += min(clw, aclw)
        cur = ord(s[i]) - 65
    return res

print(getTime("BZA"))