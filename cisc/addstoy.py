"""
    Given X and Y
    Return arr[i], where i <= X and digits of i adds up to Y
    Ex: X = 20 and Y = 5, so ans = [14, 5]
"""

def addtoy(x: int, y: int):
    values = []
    h, d, e= 0, 0, 0
    for i in range(x):
        temp = i
        e = temp % 10
        d = ((temp - e) // 10) % 10
        h = temp // 100
        print(h, d, e)
        if e + d + h == y:
            values.append(temp)
    print(values)

x = 173
y = 5
addtoy(x, y)