# import sys
# sys.stdin = open("input.txt","r")

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    N //= 10

    def get_point(num):

        arr = [0] * num
        arr[0] = 1

        for i in range(1,num):
            if (i+1) % 2 == 0:
                arr[i] = arr[i-1] * 2 + 1
            else:
                arr[i] = arr[i-1] * 2 - 1

        return arr[num-1]

    ans = get_point(N)
    print(f"#{tc} {ans}")