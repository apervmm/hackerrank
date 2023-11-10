# Write any import statements here

def getArtisticPhotographCount(N: int, C: str, X: int, Y: int) -> int:
    count = 0
    startAt = next((pos for pos in range(len(C)) if C[pos] in ['P', 'B']), N)
    print("strart: ", startAt)
    for i in range(startAt, N):
        if C[i] == 'A':
            left = C[max(0, i-Y):max(0, i-X+1)]
            right = C[min(i+X, N):min(i+Y+1, N)]
            pabs = sum(1 for p in left if p == 'P') * sum(1 for b in right if b == 'B')
            baps = sum(1 for b in left if b == 'B') * sum(1 for p in right if p == 'P')
            count += pabs + baps
    return count


print(getArtisticPhotographCount(5, "APABA", 1, 2))
print(getArtisticPhotographCount(5, "APABA", 2, 3))
print(getArtisticPhotographCount(8, ".PBAAP.B", 1, 3))

