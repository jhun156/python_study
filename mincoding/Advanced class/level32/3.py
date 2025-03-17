import sys
sys.stdin = open("input.txt","r")

N = int(input())
arr = list(map(int,input().split()))

for i in range(N-2):
    if arr[i] == arr[i+1] == arr[i+2]:
        arr[i],arr[i+1],arr[i+2] = 'x','x','x'

