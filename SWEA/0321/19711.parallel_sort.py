# import sys
# sys.stdin = open("input.txt","r")


def merge_sort(Left,Right):

    global ans
    result = []

    while Left and Right:
        if Left[0] <= Right[0]:
            result.append(Left[0])
            Left.pop(0)
        else:
            result.append(Right[0])
            Right.pop(0)

    if Left:
        ans += 1
        result.extend(Left)
        return result

    else:
        result.extend(Right)
        return result


def divide(lst):

    if len(lst) == 1:
        return lst

    mid = len(lst) // 2
    left = lst[:mid]
    right = lst[mid:]
    last_left = divide(left)
    last_right = divide(right)

    return merge_sort(last_left,last_right)


T = int(input())
for tc in range(1,T+1):
    L = int(input())
    arr = list(map(int,input().split()))
    ans = 0

    divide(arr)
    print(f"#{tc} {ans}")