"""
    Given an integer n, return the number of strings of length n that consist only of vowels (a, e, i, o, u) and are lexicographically sorted.

    A string s is lexicographically sorted if for all valid i, s[i] is the same as or comes before s[i+1] in the alphabet.

    Example 1:
        Input: n = 2
        Output: 15
        Explanation: The 15 sorted strings that consist of vowels only are
        ["aa","ae","ai","ao","au","ee","ei","eo","eu","ii","io","iu","oo","ou","uu"].
        Note that "ea" is not a valid string since 'e' comes after 'a' in the alphabet.
"""

def countVowelStrings( n: int) -> int:
    # O(1), T(1)
    return (n + 4) * (n + 3) * (n + 2) * (n + 1) // 24

def countDP(n: int) -> int:
    # O(n)
    dp = [1] * 5

    for _ in range(1,n):
        for i in range(1,5):
            dp[i] += dp[i-1]
        print(dp)
    #print(dp)
    return sum(dp)



print(countDP(3))


#print(countVowelStrings(10))