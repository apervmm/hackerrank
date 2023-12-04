
from typing import List
from collections import Counter


def getTripletCountN3(stock, d):
    count = 0
    for i in range(len(stock) - 2):
        for j in range(i+1, len(stock) -1):
            for k in range(j+1, len(stock)):
                if (stock[i] + stock[j] + stock[k]) % d == 0:
                    count +=1 
    return count


def solve(nums, d):
    n = len(nums)
    counter = Counter()
    res = 0
    for j in range(n-2,-1,-1):
        counter[nums[j+1]%d] += 1
        for i in range(j):
            res += counter[-(nums[i]+nums[j])%d] 
    print(counter)
    return res



def main():
    stock = [3, 3, 4, 7, 8]
    a = solve(stock, 5)
    print(a)
    


main()