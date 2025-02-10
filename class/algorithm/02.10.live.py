# 검색 : 저장되어 있는 자료 중에서 원하는 항목을 찾는 작업

# 순차 검색 (Sequential Search)

def sequential_search1(a,n,key):
    i = 0
    while i < n and a[i] != key:
        i += 1
        if i < n:
            return i
        else:
            return -1

def sequential_search2(a,n,key):
    for i in range(n):
        if a[i] == key:
            return i
    return -1

def sequential_search3(a,n,key):
    i = 0
    while i < n and a[i] < key:
        i += 1
        if i < n and a[i] == key:
            return i
        else:
            return -1

# 이진 검색 (Binary Search)

def binary_search1(a,n,key):
    start = 0
    end = n - 1
    while start <= end:
        middle = (start + end)//2
        if a[middle] == key:
            return middle
        elif a[middle] > key:
            end = middle - 1    # end 초기화
        else:
            start = middle + 1  # start 초기화
    return -1

def binary_search(a,n,key):
    start = 0
    end = n - 1
    while start <= end:         # 검색 구간에 1개 이상의 원소가 있으면 검색
        middle = (start + end) // 2
        if a[middle] == key:
            return middle
        elif a[middle] > key:
            end = middle - 1
        elif a[middle] < key:
            start = middle + 1
    return -1                   # 검색 실패, 찾는 값이 없는 경우

# 선택 정렬

arr = [3,1,7,2,4,8,5,6] # n = 8

for i in range(7):
    for j in range(i+1,8):
        if arr[i] > arr[j]:
            arr[i],arr[j] = arr[j],arr[i]
print(arr)

# 카운팅 정렬

arr = [3,1,7,2,4,8,5,6] # n = 8

target = [0] * 10

for i in range(8):
    target[arr[i]] += 1

for i in range(1,10):
    target[i] += target[i-1]

sorted_arr = [0] * 8

for i in range(8):
    target[arr[i]] -= 1
    index = target[arr[i]]
    sorted_arr[index] = arr[i]

print(sorted_arr)

# 버블 정렬

arr = [3,1,7,2,4,8,5,6] # n = 8

for i in range(7,-1,-1):
    for j in range(i):
        if arr[j] > arr[j+1]:
            arr[j],arr[j+1] = arr[j+1],arr[j]
print(arr)

# 삽입 정렬

arr = [3,1,7,2,4,8,5,6] # n = 8
sorted_arr = []

for i in range(8):
    sorted_arr.append(arr[i])
    for j in range(i,0,-1):
        if sorted_arr[j] < sorted_arr[j-1]:
            sorted_arr[j],sorted_arr[j-1] = sorted_arr[j-1],sorted_arr[j]
print(sorted_arr)

def select(arr,k):
    for i in range(0,k):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[min_index] > arr[j]:
                min_index = j
        arr[i],arr[min_index] = arr[min_index],arr[i]
    return arr[k-1]
