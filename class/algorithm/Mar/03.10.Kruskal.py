# Kruskal algorism
# 최소 연결 간선 관련 문제

import sys
sys.stdin = open("input.txt","r")

k = int(input())
n = int(input())
lst = [list(input().split()) for _ in range(n)]
lst.sort(key=lambda x:int(x[2]))
arr = [0] * 200

total = 0
cnt = 0

def union(a,b,index):

    global total, cnt
    boss_a, boss_b = findboss(a), findboss(b)
    if boss_a == boss_b:
        return
    total += int(lst[index][2])
    cnt += 1
    arr[ord(boss_b)] = boss_a

def findboss(num):

    if arr[ord(num)] == 0:
        return num
    ret = findboss(arr[ord(num)])
    arr[ord(num)] = ret
    return ret

for i in range(n):

    if cnt == k - 1:
        print(total)
        break
    union(lst[i][0],lst[i][1],i)

