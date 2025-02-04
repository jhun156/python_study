arr =[
    ['A','7','9','T','K','Q'],
    ['M','I','N','C','O','D'],
]

lst = list(input().split())

def isExist(str):
    global arr
    for i in range(2):
        for j in range(6):
            if arr[i][j] == str:
                return 1
    return 0

for i in lst:
    ret = isExist(i)
    if ret == 1:
        print(f"{i} : 존재")
    else:
        print(f"{i} : 없음")