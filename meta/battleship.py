from typing import List
import secrets

# Write any import statements here

def getHitProbability(R: int, C: int, G: List[List[int]]) -> float:
    # Write your code here
    # r = random.randint(0, R)
    # c = random.randint(0, C)
    shots = R * C
    success = 0
    for i in range(R*C):
        r = secrets.SystemRandom().randint(0, R)
        c = secrets.SystemRandom().randint(0, C)
        if G[r][c] == 1:
            success += 1

    return success/shots
