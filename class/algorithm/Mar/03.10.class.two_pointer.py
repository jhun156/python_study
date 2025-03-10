# 구간합
# 1. Sliding Window  구간의 크기가 정해져있을 때
# 2. Two pointer

import sys
sys.stdin = open("input.txt","r")

n,m = map(int,input().split())   # target
arr = list(map(int,input().split()))
low = high = 0
Sum = cnt = 0

while low != n:

    if Sum >= m or high == n:
        Sum -= arr[low]
        low += 1
    elif Sum < m:
        Sum += arr[high]
        high += 1
    if Sum == m:
        cnt += 1

print(cnt)

'''
# 강사님 코드
n,m=map(int,input().split())       # 11 5
arr=list(map(int,input().split())) # 1 2 3 4 2 5 3 1 1 2 5
cnt,Sum=0,0
right,left=0,0
target=m
while 1:
    if Sum>=target or right==n:
        Sum-=arr[left]
        left+=1
    elif Sum<target:
        Sum+=arr[right]
        right+=1
    if Sum==target:
        cnt+=1
    if left==n:
        break
print(cnt)

'''

