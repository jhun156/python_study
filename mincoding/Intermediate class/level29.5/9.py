# 새로운 풀이
text1 = input()
text2 = input()
len1 = len(text1)
len2 = len(text2)

arr = [[0] * (len2+1) for _ in range(len1+1)]
Max = 0
idx = 0

for i in range(1,len1+1):
    for j in range(1,len2+1):
        if text1[i-1] == text2[j-1]:
            arr[i][j] = arr[i-1][j-1] + 1
            if arr[i][j] > Max:
                Max = arr[i][j]
                idx = j

print(text2[idx-Max:idx])