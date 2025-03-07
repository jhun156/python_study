import sys
sys.stdin = open("input.txt","r")

def insert(num):

    while True:
        p = num // 2
        if p == 0:
            return
        elif num % 2 == 0:
            if arr[p] < arr[num]:
                arr[p],arr[num] = arr[num],arr[p]
                align(p)
                num = p
            else:
                return
        elif num % 2 == 1:
            if arr[p] > arr[num]:
                arr[p],arr[num] = arr[num],arr[p]
                align(p)
                num = p
            else:
                return

def align(num):

    while True:
        if arr[num*2] > arr[num]:
            arr[num],arr[num*2] = arr[num*2],arr[num]
        elif arr[num*2+1] != 0 and arr[num*2+1] < arr[num]:
            arr[num], arr[num*2+1] = arr[num*2+1], arr[num]
        if arr[num*2+1] == 0:
            return
        elif arr[num*2] < arr[num] < arr[2*num+1]:
            return

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [0] * (2*N+2)

    for i in range(1,N+1):
        arr[i] = i
        insert(i)

    print(f"#{tc} {arr[1]} {arr[N//2]}")

