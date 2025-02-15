# join
# string = "a b c d"
# "".join(string)
# print()
'''
txt = list(input())
N = len(txt)
for i in range(N//2):
    txt[i],txt[N-1-i] = txt[N-1-i],txt[i]
print(txt)
'''
# 문자열 뒤집기
# 1)
s1 = 'string'
s = s1[::-1]
print(s)
# 2)
s = 'abcd'
s = list(s)
s.reverse()
s = ''.join(s)
print(s)

# 1215. 회문
n = int(input())
for j in range(8-n):
    for k in range(N//2):
        if txt[j+k] != txt[j+N-1-k]:
            break
    else:
        total += 1

def atoi(s):
    i = 0
    for x in s:
        i = i * 10 + ord(x) - ord('0')
    return i

a = input()
ans = atoi(a)
print(ans)







