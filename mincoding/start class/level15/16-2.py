a = input()
n = ord(a)

arr = [[0] * 3 for _ in range(3)]

i = 1
while i < 4:
    j = 0
    while j < i:
        arr[3-i][j] = n
        n += 1
        j += 1
    i += 1

for i in range(3):
    for j in range(3):
        if arr[i][j] != 0:
            print(chr(arr[i][j]),end='')
        else:
            print(' ',end='')
    print()
