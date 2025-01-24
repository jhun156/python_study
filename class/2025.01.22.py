# def abc():
#     print("aaaa")

# for i in range(2):           # 함수가 종료되면 호출한 곳으로 돌아감.
#     abc()

# def get_sum(a,b):            # a,b 매개변수 parameter
#     print(a+b)
#     return           # return을 만나는 순간 함수가 끝남

# get_sum(3,7)        # 3,7 인자값 argument

# 예시  - argument / parameter 개수가 다를때
# 1. default parameter

# def get_sum(a,b,c=3):           
#     return a+b+c            # default 값은 맨 뒤에 쓴다

# ret = get_sum(1,2)          
# print(ret)        

# 2. packing / unpacking 을 사용하는 경우

# num = [1,2,3,4,5]           # list 자체가 packing
# num2 = (1,2,3,4,5)

# print(num,num2)

# a,b,*c = num2             # unpacking
# print(a,b,c)
# print(c)

# def getsum(*a):
#     print(type(a))
#     return a[0]+a[1]+a[2]

# result = getsum(1,2,3)
# print(result)

# # 3. keyword 가변인자

# def print_info(**args):
#     print(args)
#     print(type(args))
#     for i,j in args.items():
#         print(i,j)

# print_info(kevin=1,john=2,bob=3)

# ☆☆☆ 4. 지역변수 전역변수

# aa = 6

# def abc():
#     aa=3    # 지역변수
#     bb=5
#     print(aa,bb)

# abc()
# print(aa)

# aa = 3
# bb = 5

# def test():
#     global aa
#     aa = aa + 1
#     print(aa,bb)

# test()

# 전역변수

# def KFC():
#     global aa,bb
#     print(aa,bb)
#     aa += 1
#     bb += 1
#     print(aa,bb)

# def test():
#     global aa,bb
#     aa = 3
#     bb = 5
#     print(aa,bb)

# test()
# KFC()

# 파이썬 내장함수 중 - map, zip, filter, lambda 
# map - 리스트나 튜플같이 순회가 가능한 데이터구조의 값에 일괄적으로 함수를 적용할 때 사용
#     - 반환값은 map 객체를 반환
#     - map(함수, iterables)

# num = ['1','2','3']
# lst1 = []
# for i in num:
#     lst1.append(int(i))

# print(lst1)

# lst2 = map(int,num)
# print(lst2)
# print(list(lst2))

# a,b,c = map(int,input().split())
# print(a,b,c)

# lst=list(map(int,input().split()))
# print(lst)

# zip - 순회가능한 객체를 인자로 받고 각 요소를 잘라서
#     - 튜플을 원소로 하는 객체를 반환한다.

# a = '12345'
# b = 'qwert'
# c = 'asdfg'

# for i in zip(a,b,c):
#     print(list(i))

# for x,y,z in zip(a,b,c):
#     print(x,y,z)

# arr=[
#     [1,2,3],
#     [4,5,6],
#     [7,8,9],
# ]

# arr = list(map(list,zip(*arr)))

# for i in zip(arr[0],arr[1],arr[2]):
#     print(list(i))

# for i in zip(*arr):
#     print(list(i))

# arr=list(map(list,zip(*arr)))
# print(arr)

# filter 함수
# list나 tuple과 같이 순회가능한 데이터구조의 값들에 함수를 적용
# 적용후 값이 True 인 것들만 반환 (filter 라는 객체로 반환)

# num = list(range(1,10))

# def get_even(value):

#     # if value%2==0:
#     #     return True
#     # else:
#     #     return False
#     return True if value % 2==0 else False

# ret = filter(get_even(num))
# print(list(ret))

# lambda 이름이 없는 익명 함수

# def Sum(a,b):
#     return a+b

# result = Sum(3,5)
# print(result)

# result = (lambda a,b : a + b)(3,5)
# print(result)

# result = (lambda a,b : a+b)
# print(result(3,5))

# 재귀함수 recursion

# n = int(input())

# path = [0]*n

# def abc(level):
#     if level == n:
#         for i in range(n):
#             print(path[i],end=' ')
#         print()
#         return
#     for i in range(6):
#         path[level]=i+1
#         abc(level+1)

# abc(0)

# [연습문제]
# 두 리스트값을 세로로 더했을때 합을 각각 출력하기

# lst1 = [1,2,3,4,5]
# lst2 = [6,7,8,9,10]

# result = print(*list(map(lambda x, y : x + y ,lst1,lst2)))

# [연습문제]
# 0~100 정수중 짝수만 리스트에 담아서 출력

# result = filter(lambda even:even%2==0,range(100))
# print(list(result))

# def abc():

#     global tae

#     lst[0]=100
#     arr = [100,2,3]
#     tae = [100,2,3]

# lst = [1,2,3]
# arr = [1,2,3]
# tae = [1,2,3]

# abc()

# print(lst)
# print(arr)
# print(tae)

# 리스트 안의 값만 바꿀때는 잘 된다
# 리스트 자체를 재할당할때는 global을 써야한다.

# 2차원 리스트

# def abc():
#     mc[0][0] = 100
#     kfc[0] = [100,2,3]
#     bbq = [[100,2,3],[4,5,6]]

# mc = [
#     [1,2,3],
#     [4,5,6],
# ]
# kfc = [
#     [1,2,3],
#     [4,5,6],
# ]
# bbq = [
#     [1,2,3],
#     [4,5,6],
# ]

# abc()

# print(*mc)
# print(*kfc)
# print(*bbq)

# 결론
# 변수의 경우 전역변수의 값을 바꾸는 경우가 아니라면 global 생략가능
# 리스트의 경우 리스트의 값을 바꾸는 것은 global 생략가능, 그러나 재할당은 반드시 global 써야 가능