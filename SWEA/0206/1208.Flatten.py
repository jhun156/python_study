import sys
sys.stdin = open("input.txt","r")

T = 10
for test_case in range(1,T+1):
    dump_count = int(input())
    box_list = [i for i in map(int,input().split())]    # box 개수는 항상 100개
    count = 0
