# import sys
# sys.stdin = open("input.txt","r")

arr = [list(map(int,input().split())) for _ in range(4)]
for i in range(1,4):
    arr[0][i] += arr[0][i-1]
    arr[i][0] += arr[i-1][0]

for i in range(1,4):
    for j in range(1,4):
        arr[i][j] = min(arr[i-1][j],arr[i][j-1]) + arr[i][j]

def Print(y,x):

    if y == 0 and x == 0:
        print(f"{y},{x}")
        return

    if y == 0:
        Print(0,x-1)
        print(f"{y},{x}")
    elif x == 0:
        Print(y-1,0)
        print(f"{y},{x}")
    else:
        if arr[y-1][x] < arr[y][x-1]:
            Print(y-1,x)
            print(f"{y},{x}")
        else:
            Print(y,x-1)
            print(f"{y},{x}")


Print(3,3)