# Union-find 구조 Cycle 확인

import sys
sys.stdin = open("input.txt","r")

n, m = map(int,input().split())
edge = []
for _ in range(m):
    edge.append(input().split())

flag = 0
arr = [0] * 200

def union(a,b):

    A,B = find(a),find(b)
    if A == B:
        return 1
    arr[ord(B)] = A

def find(num):

    if arr[ord(num)] == 0:
        return num
    ret = find(arr[ord(num)])
    arr[ord(num)] = ret
    return ret

for i in range(m):
    a,b = edge[i]
    ret = union(a,b)
    if ret:
        flag = 1
        break

if flag:
    print("Cycle 발생")
else:
    print("Cycle X")
