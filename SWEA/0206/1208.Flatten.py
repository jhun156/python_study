# import sys
# sys.stdin = open("input.txt","r")

T = 10
for test_case in range(1, 11):
    dump_count = int(input())
    box_list = list(map(int, input().split()))
    cnt = 0
    while cnt < dump_count and max(box_list) - min(box_list) > 2:
        max_index = box_list.index(max(box_list))
        min_index = box_list.index(min(box_list))
        box_list[max_index] -= 1
        box_list[min_index] += 1
        cnt += 1
    ans = max(box_list) - min(box_list)
    print(f"#{test_case} {ans}")