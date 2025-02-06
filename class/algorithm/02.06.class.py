# 시간복잡도 (Time Complexity) 계산
# 기본 연산 수행 횟수 + 입력되는 data 값의 범위
# 종합적으로 고려해서 계산을 하는 "점근적 표기법"
# 최악표기법 : 주로 사용하게 될 기법 O(n) 표기법
# 평균표기법 : 크게 중요x
# 최선표기법 : 크게 중요x
# PS (Problem Solving) 최악표기법으로 계산(빅-오 표기법)
# 1억번 계산당 1초로 계산

# import sys
# sys.stdin = open("input.txt", "r")

# for문 돌다가 6의 좌표값 출력
# arr = [list(map(int,input().split())) for _ in range(3)]
# Max,num = 0,0
# lst = []
# for i in range(3):
#     result = 0
#     for j in range(3):
#         result += arr[i][j]
#     lst.append(result)
# Max_value = 0
# Max_i = lst[0]
# for i in lst:
#     if Max_i < i:
#         Max_i = i
# print(Max_i)
# for i in lst:
#     Max_value += i
# print(Max_value)
'''
# 강사님 코드
Max = -21e8
Max_index = 0
for i in range(3):
    Sum = 0
    for j in range(4):
        Sum += arr[i][j]
    if Sum > Max:
        Max = Sum
        Max_index = i + 1
print(Max)
print(Max_index)
'''
# 리스트에 숫자 6개를 입력받으세요. 그리고 누적합을 구하세요~~

# 3 7 4 2 9 5 입력시 30 25 16 14 10 3 출력
'''
arr = list(map(int,input().split()))
for i in range(1,6):
    arr[i] += arr[i-1]
for i in range(5,-1,-1):
    print(arr[i], end=' ')
'''
# 문자열 1개 그리고 정수값 1개 입력
#
# 입력받은 정수값 만큼 문자열을 우측으로 회전시킨 후
# 문자열을 출력하기
#
# apple 3입력시 pleap 출력하기
'''
내 코드
a = input()
num = int(input())
lst = [0] * len(a)
for i in range(len(a)):
    if i + num <= len(a) - 1:
        lst[i+num] = a[i]
    else:
        lst[(i+num)%len(a)] = a[i]
string = ''
for i in lst:
    string += i
print(string)
'''

# 강사님 코드
'''
lst = list(input())
n = int(input())
a_len = len(lst)
for i in range(n%a_len):
    temp = lst[-1]
    for i in range(a_len-1,0,-1):
        lst[i] = lst[i-1]
    lst[0] = temp
'''
'''
두 리스트 하드코딩 후 (lst / target)
lst=[[4, 2, 3, 5],
     [1, 1, 2, 3],
     [4, 7, 6, 4]]
target=[[8, 4],
        [2, 9]]
target이 lst에 존재여부 y 또는 n 으로 출력하기
'''
'''
lst=[[4, 2, 3, 5],
     [1, 1, 2, 3],
     [4, 7, 6, 4]]
target=[[1, 2],
        [7, 6]]
def Findpt(y,x):
    for i in range(2):
        for j in range(2):
            if target[i][j] != lst[y+i][x+j]:
                return 0
    return 1

for i in range(2):
    for j in range(3):
        ret = Findpt(i,j)
        if ret == 1:
            break
    if ret == 1:
        break
if ret == 1:
    print("찾음")
else:
    print("없음")
'''
'''
# 내 코드
lst=[[4, 2, 3, 5],
     [1, 1, 2, 3],
     [4, 7, 6, 4]]
target=[[1, 2],
        [7, 6]]
arr = []
for i in range(2):
    for j in range(2):
        count = 0
        for x in range(3):
            for y in range(4):
                if target[i][j] == lst[x][y]:
                    count += 1
        arr.append(count)
print(arr)
'''
'''
# 강사님 코드
def isExist(value):
    count = 0
    for i in range(3):
        for j in range(4):
            if lst[i][j] == value:
                count += 1
    return count

for i in range(2):
    for j in range(2):
        ret=isExist(target[i][j])
        print(f"{target[i][j]}:{ret}")
'''
'''
# 선택정렬
arr = [4,7,1,2,3,9,6]
for i in range(6):
    for j in range(i+1,7):
        if arr[i] > arr[j]:
            arr[i],arr[j] = arr[j],arr[i]
print(arr)

lst = [2,7,1,8,3,4]
for i in range(len(lst)-1):
    for j in range(i+1,len(lst)):
        if lst[i] > lst[j]:
            lst[i],lst[j] = lst[j],lst[i]
print(*lst)
'''
'''
# 삽입정렬
arr = [3,7,2,5,4,8]
lst = []
for i in range(6):
    lst.append(arr[i])
    for j in range(i,-1,-1):
        if lst[j-1] > lst[j]:
            lst[j-1],lst[j] = lst[j],lst[j-1]
        else:
            break
print(*lst)
# 평균적으론 O(n2)의 속도가 나오지만, 이미 정렬이 많이 된 배열에 하나를 추가해서 정렬할때
# O(n)에 가까운 속도가 나온다.
'''

# 버블정렬

arr = [1,2,5,3,7,1,6]
for i in range(len(arr)-1,0,-1):
    for j in range(i):
        if arr[j] > arr[j+1]:
            arr[j],arr[j+1] = arr[j+1],arr[j]
print(arr)

arr = [1,2,5,3,7,1,6]
for i in range(len(arr)-1,0,-1):
    for j in range(len(arr)-2,len(arr)-2-i,-1):
        if arr[j] > arr[j+1]:
            arr[j],arr[j+1] = arr[j+1],arr[j]
print(arr)

































