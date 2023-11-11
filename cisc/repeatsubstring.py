

def repeat(s: str):
    i, b, e = 0, 0, 0
    result = []
    while i < len(s):
        char = s[i]
        if char.isdigit():
            e = i
            result.append(s[b: e] * int(char))
            b = i + 1
        i += 1
    return "".join(result)

s = "ab2a3"
print(repeat(s))