def checkInclusion(s1: str, s2: str) -> bool:
    letters = {}
    for i in range(len(s1)):
        letters[s1[i]] = 1 + letters.get(s1[i], 0)

    charSet = {}

    l = 0
    for r in range(len(s2)):
        if r - l + 1 > len(s1):
            if charSet.get(s2[l]) != 1:
                charSet[s2[l]] -= 1
            else:
                charSet.pop(s2[l])
            l += 1

        charSet[s2[r]] = 1 + charSet.get(s2[r], 0)

        if charSet == letters:
            return True
    print(letters)
    print(charSet)
    return False


s1 = "ab"
s2 = "a"

print(checkInclusion(s1 ,s2))