"""
Rotate Matrix by 90 deg in-place

"""

from typing import List


def rotateCLK(matrix: List[List[int]]) -> List[List[int]]:
    l, r = 0, len(matrix) - 1

    while l < r:
        for i in range(r - l):
            top, bottom = l, r

            #save top left
            topLeft = matrix[top][l + i]

            #move bottom left intp top left
            matrix[top][l + i] = matrix[bottom - i][l]

            #move bottom r to bottom l
            matrix[bottom - i][l] = matrix[bottom][r - i]

            # top rigth to bottom right
            matrix[bottom][r - i] = matrix[top + i][r]

            # topLeft to topRight
            matrix[top + i][r] = topLeft
            
        r -= 1
        l += 1
    return matrix

def rotateACLK(matrix: List[List[int]]) -> List[List[int]]:
    left, right = 0, len(matrix) - 1

    while left < right:
        for i in range(right- left):
            top, bottom = left, right

            #save TopLeft
            topLeft = matrix[top + i][left]

            # topRight -> topLeft
            matrix[top + i][left] = matrix[top][right - i]

            # bottomRight -> topRight
            matrix[top][right - i] = matrix[bottom - i][right]

            #bottomLeft -> bottomRight
            matrix[bottom - i][right] = matrix[bottom][left + i]

            # Saved TopLeft -> bottomLeft
            matrix[bottom][left + i] = topLeft
        right -= 1
        left += 1
    return matrix


matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]

m = rotateACLK(matrix)

for i in m:
    print(i)
    