#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    ls, hs = 0, 0
    low, high = scores[0], scores[0]
    for i in range(1, len(scores)):
        if scores[i] > high:
            high = scores[i]
            hs += 1
        if scores[i] < low:
            low = scores[i]
            ls += 1
    print(hs, ls)
    return [hs, ls]
    


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
