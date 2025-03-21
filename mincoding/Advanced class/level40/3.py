arr = list(map(int,input().split()))

for i in range(3,12):
    a = arr[i-2] + arr[i]
    b = arr[i-3] + arr[i]
    c = arr[i//2] + arr[i]
    if i % 2 == 0:
        arr[i] = max(a,b,c)
    else:
        arr[i] = max(a,b)

print(max(arr[6:]))