arr = [list(input()) for _ in range(3)]

ans = []

for i in range(3):
    n = len(arr[i])
    for j in range(n,-1,-1):
