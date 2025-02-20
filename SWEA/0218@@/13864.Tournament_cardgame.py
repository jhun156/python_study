import sys
sys.stdin = open("input.txt","r")



T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = list(map(int,input().split()))
    ans = 0
    # 최종으로 이긴 사람의 인덱스 + 1 이 답




    print(f"#{tc} {ans}")