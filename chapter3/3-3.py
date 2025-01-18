# test_list = ["one", "two", "three"]
# for i in test_list:
#     print(i)

a = [(1,2), (3,4), (5,6)]
for (first,last) in a:
    print(first+last)

# for문 : list나 tuple에 있는 것을 하나씩 뽑아올 때 사용
# while문 : 조건을 만족하거나 또는 여러개의 행동을 반복할 때 사용

# marks = [90, 25, 67, 45, 80]   # 학생들의 시험 점수 리스트

# number = 0   # 학생에게 붙여 줄 번호
# for mark in marks:   # 90, 25, 67, 45, 80을 순서대로 mark에 대입
#     number = number +1 
#     if mark < 60: 
#         continue
#     print("%d번 학생은 합격입니다. 축하합니다" % number)

# add = 0
# for i in range(1,11):
#     add += i
#     print(add)

# 구구단
# for i in range(2,10):
#     for j in range(1,10):
#         print(i*j, end=" ")
#     print("\n")
# print("구구단이 끝났습니다")

# a = [1, 2, 3, 4]
# result = [num*3 for num in a]

# print(result)

# a = [1, 2, 3, 4]
# result = [num * 3 for num in a if num % 2 == 0]

# print(result)

# result = []
# for num in a:
#     if num % 2 == 0:
#         result.append(num*3)

# print(result)

result = [x*y for x in range(2,10) for y in range(2,10)]

print(result)