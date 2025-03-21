arr = list(input())
K = int(input())
N = len(arr)
Max = -1000
visited = set()

def two_score(st,ed):

    ret = 0
    if arr[st] == arr[ed]:
        ret = -50
    elif abs(ord(arr[st])-ord(arr[ed])) <= 5:
        ret = 3
    elif abs(ord(arr[st])-ord(arr[ed])) >= 20:
        ret = 10
    return ret

def three_score(st,mid,ed):

    ret = 0
    if arr[st] == arr[mid] or arr[mid] == arr[ed]:
        ret = -50
    elif abs(ord(arr[st])-ord(arr[mid])) <= 5 and abs(ord(arr[mid])-ord(arr[ed])) <= 5:
        ret = 3
    elif abs(ord(arr[st])-ord(arr[mid])) >= 20 and abs(ord(arr[mid])-ord(arr[ed])) >= 20:
        ret = 10
    return ret


def dfs(level):

    global Max,cnt
    cnt += 1
    if level == K:
        score = 0
        for i in range(N):
            if i == 0:
                score += two_score(0,1)
            elif 0 < i < N - 1:
                score += three_score(i-1,i,i+1)
            else:
                score += two_score(N-2,N-1)

        Max = max(Max,score)
        return

    arr_tuple = tuple(arr)
    if arr_tuple in visited:
        return
    visited.add(arr_tuple)

    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            arr[i],arr[j] = arr[j],arr[i]
            dfs(level+1)
            arr[i], arr[j] = arr[j], arr[i]


cnt = 0
dfs(0)
print(Max)
print(cnt)