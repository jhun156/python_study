# 정렬 종류

# 선택, 삽입, 버블 - n**2
# 힙, 합병, 퀵 - n log n
# 계수정렬 - n

'''
# merge sort 민코딩 29.5 - 4번 문제
arr = [2,7,5,3,1,5,9,2]

def merge(start,end):

    global arr
    mid = (start+end) // 2

    if start == end:
        return

    merge(start,mid)
    merge(mid+1,end)

    a = start
    b = mid + 1
    result = []

    while 1:
        if a > mid and b > end:
            break
        if a > mid:
            result.append(arr[b])
            b += 1
        elif b > end:
            result.append(arr[a])
            a += 1
        elif arr[a] < arr[b]:
            result.append(arr[a])
            a += 1
        else:
            result.append(arr[b])
            b += 1

    for i in range(len(result)):
        arr[start+i] = result[i]

merge(0,7)
print(*arr)
'''


# quick sort 민코딩 23.5 - 5번
arr=[4,1,7,9,6,3,3,6]

def quick(start,end):

    if start >= end:
        return
    pivot = start
    a = start+1
    b = end

    while 1:

        while a <= end and arr[a] <= arr[pivot]:
            a += 1

        while b >= start and arr[b] > arr[pivot]:
            b -= 1

        if a > b:
            break
        arr[a], arr[b] = arr[b], arr[a]

    arr[pivot], arr[b] = arr[b], arr[pivot]

    quick(start, b-1)
    quick(b+1, end)


quick(0,7)
print(*arr)