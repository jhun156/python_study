# import sys
# sys.stdin = open("input.txt","r")

T = int(input())
for tc in range(1,T+1):
    n = int(input())
    lst = list(range(10))

    def count_sheep(num):
        global lst
        a = str(num)
        tmp_lst = list(map(int,a))
        n = len(tmp_lst)
        for i in range(n):
            if tmp_lst[i] in lst:
                lst.remove(tmp_lst[i])
        if len(lst) == 0:
            return 1
        else:
            return 0

    for i in range(1,100000):
        ans = count_sheep(n*i)
        if ans == 1:
            print(f"#{tc} {i}")
            break