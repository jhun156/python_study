arr = []
a = 1
for i in range(7):
    row = []
    for j in range(4):
        row.append(a)
        a += 1
    arr.append(row)

revise = list(map(int,input().split()))

for i in range(4):
    for j in revise:
        arr[j][i] = 0

for i in range(7):
    print(*arr[i])