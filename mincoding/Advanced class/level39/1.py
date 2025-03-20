arr = list(map(int,input().split()))
Sum = 0
N = len(arr)

cnt = 0
while cnt < N - 1:
    tmp = arr.pop(arr.index(min(arr)))
    Sum += len(arr) * tmp
    cnt += 1

print(Sum)