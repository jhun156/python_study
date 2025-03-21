arr = [list(map(int,input().split())) for _ in range(7)]

for i in range(1,7):
    a = arr[i-1][0]
    b = arr[i-1][1]
    c = arr[i-1][2]
    if a == 0:
        a = -21e8
    if b == 0:
        b = -21e8
    if c == 0:
        c = -21e8
    if arr[i][0] != 0:
        arr[i][0] += max(a,b)
    if arr[i][1] != 0:
        arr[i][1] += max(a,b,c)
    if arr[i][2] != 0:
        arr[i][2] += max(b,c)

print(max(arr[6]))