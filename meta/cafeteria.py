from typing import List
import math


def getMaxAdditionalDinersCount(N: int, K: int, M: int, S: List[int]) -> int:
    S.sort()
    extraSapce = 0
    firstOpenSeat = 1
    for takenSeat in S:
        openSeats = takenSeat - K - firstOpenSeat
        if openSeats > 0:
            extraSapce += math.ceil(openSeats/(K + 1))
        firstOpenSeat = takenSeat + K + 1
    openSeats = N + 1 - firstOpenSeat
    if openSeats > 0:
            extraSapce += math.ceil(openSeats/(K + 1))
    return extraSapce
  

print(getMaxAdditionalDinersCount(10, 1, 2, [2, 6]))