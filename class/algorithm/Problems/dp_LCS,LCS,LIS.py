# LCS 최장 공통 부분 문자열 Longest Common Substring
# LCS 최장 공통 부분 수열 Longest Common Subsequence
# LIS 최장 증가 부분 수열 Longest Increasing Subsequence


# 문자열 2개중 가장 긴 공통부분의 길이 구하기
# LCS 최장 공통 부분 문자열 Longest Common Substring
def lcs(s1, s2):
    len1 = len(s1)
    len2 = len(s2)
    arr = [[0] * (len1+1) for _ in range(len2+1)]
    Max = 0
    for i in range(1,len1+1):
        for j in range(1,len2+1):
            if s1[i-1] == s2[j-1]:
                arr[i][j] = arr[i-1][j-1] + 1
                Max = max(Max,arr[i][j])
            else:
                arr[i][j] = 0
    return Max

s1 = 'BABJYP'
s2 = 'ABCBJY'
print(lcs(s1, s2))

# LCS 최장 공통 부분 수열 Longest Common Subsequence

def lcs(s1,s2):
    len1,len2=len(s1),len(s2)
    arr=[[0]*(len2+1) for _ in range(len1+1)]

    for i in range(1,len1+1):
        for j in range(1,len2+1):
            if s1[i-1]==s2[j-1]:
                arr[i][j]=arr[i-1][j-1]+1
            else:
                arr[i][j]=max(arr[i-1][j],arr[i][j-1])
    return arr[len1][len2]

s1="BABJYP"
s2="ABPABY"
print(lcs(s1,s2))