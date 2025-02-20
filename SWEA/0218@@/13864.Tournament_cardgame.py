import sys
sys.stdin = open("input.txt","r")

def GBB(a,b):
    if arr[a] == arr[b]:
        return a
    elif abs(arr[a]-arr[b]) == 1:
        if arr[a] > arr[b]:
            return a
        else:
            return b
    elif abs(arr[a]-arr[b]) == 2:
        if arr[a] > arr[b]:
            return b
        else:
            return a

def divide(arr):
    n = len(arr)
    if n == 1:
        return arr
    mid = (n-1)//2 + 1
    front = arr[:mid]
    back = arr[mid:]

    front = divide(front)
    back = divide(back)
    return GBB(front[0],back[0])

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = list(map(int,input().split()))
    arr.insert(0,0)  # 0번 인덱스에 0을 추가 인덱스 번호를 맞추기 위함
    ans = divide(list(range(1,N)))
    print(f"#{tc} {ans}")
    # 최종으로 이긴 사람의 인덱스 + 1 이 답
