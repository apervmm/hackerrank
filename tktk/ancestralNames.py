from typing import List

def romantoInt(roman: str) -> int:
    numerals = {
        "I":1, "V":5, "X":10,
        "L":50, "C":100, "D":500, "M":1000
    }
    output = 0
    for i, c in enumerate(roman):
        if i + 1 < len(roman) and numerals[c] < numerals[roman[i+1]]:
            output -= numerals[c]
        else:
            output += numerals[c]
    return output
    

def sortRoman(names: List[str]) -> List[str]:
    names.sort(key = lambda x: (x.split(" ")[0], romantoInt(x.split(" ")[1])))
    return names

a = sortRoman(["Steven XL", "Steven XVI", "David IX", "Mary XV", "Mary XIII", "Mary XX"])

print(a)