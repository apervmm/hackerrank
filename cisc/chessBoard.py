
def chessBoard(s: int):
    mat = []
    for i in range(s):
        inner = []
        for j in range(s):
            if  (i+j) % 2 == 0:
                inner.append("W")
            else:
                inner.append("B")
        mat.append(inner)
    print(mat)
chessBoard(3)

