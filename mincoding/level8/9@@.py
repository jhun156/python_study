def Input():

    arr = [i for i in map(int,input().split())]
    matrix = []
    count = 0

    for i in range(2):
        row = []
        for j in range(3):
            row.append(arr[count])
            count += 1
        matrix.append(row)
    
    return matrix

def process():

    global lst

    imag = [[0] * 4 for _ in range(3)]
    print(imag)
    for i in range(1,3):
        for j in range(1,4):
            imag[i][j] = imag[i-1][j] + imag[i][j-1] - imag[i-1][j-1] + lst[1][2]

    return imag[2][3]

def output(num):

    print(num)

lst = Input()
sum = process()
output(sum)
