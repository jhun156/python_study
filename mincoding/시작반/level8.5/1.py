arr = [i for i in map(int,input().split())]

for i in range(len(arr)):
    if arr[i] < 5:
        print(f"{i}번은 {arr[i]}점 불합격")
    elif arr[i] >= 5:
        print(f"{i}번은 {arr[i]}점 합격")
