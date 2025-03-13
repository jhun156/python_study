inf = 21e8
arr = [
    [0,5,inf,8],
    [7,0,9,inf],
    [2,inf,0,4],
    [inf,inf,3,0],
]

for ky in range(4):
    for si in range(4):
        for do in range(4):
            if arr[si][do] < arr[si][ky] + arr[ky][do]:
                arr[si][do] = arr[si][ky] + arr[ky][do]
                
# 원하는 값 사용