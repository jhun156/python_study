# 리스트 요소 최대값 구하기 (최소값도 마찬가지)
arr1 = [1,5,2,7,4,5,6,3]
max = arr1[0]
for i in range(len(arr1)):
    if max < arr1[i]:
        max = arr1[i]
print(max)

# 버블정렬(오름차순)
arr2 = [7,55,12,42,78]
for i in range(len(arr2)-1):
    for j in range(i):
        if arr2[j] > arr2[j+1]:
            arr2[j],arr2[j+1] = arr2[j+1],arr2[j]
print(arr2)

def bubblesort(arr,N):
    for i in range(N-1,0,-1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    print(*arr)

bubblesort([1,2,3,5,3,2,4],7)