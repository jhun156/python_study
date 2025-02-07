map = [
    [3,55,42],
    [-5,-9,-10],
]

pix = [[i for i in map(int,input().split())] for _ in range(2)]

def isExist(num):
    for i in range(2):
        for j in range(3):
            if map[i][j] == num:
                return 'Y'
    return 'N'

for i in range(2):
    for j in range(2):
        pix[i][j] = isExist(pix[i][j])
        print(pix[i][j],end = ' ')
    print()