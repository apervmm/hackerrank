
from typing import List

def commonSubstring(str1: List[str], str2: List[str]) -> List[bool]:
    res = []
    for i in range(len(str1)):
        aset, bset = set(str1[i]), set(str2[i])
        inter = aset.intersection(bset)
        if len(inter) == 0:
            res.append(False)
        else:
            res.append(True)
    return res


def main():
    a = ["ab", "cd", "ef"]
    b = ["af", "ee", "ef"]
    res = commonSubstring(a, b)
    print(res)

main()