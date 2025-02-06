arr = [
    [3,5,9],
    [4,2,1],
    [5,1,5],
]

# lst = [i for i in map(int,input().split())]
lst = [3,7,1]

# def isExist(a):
for i in range(3):
    for j in range(3):
        if arr[i][j] == 3:
            print(f"{3}:존재")
            

for num in lst:
    isExist(num)
