# # 변수 선언후 값 넣기

# a = 1   # 정수값 1
# b = "1" # 문자 1
# c = True    

# target = "A"

# # americano, cookie = 2000
# # americano, coke = 2000, 3000

# # 숫자
# number = 3
# # 초기화했다. 할당했다

# print(type(number))

# # 문자
# str = "문자열"
# print(type(str))

# # boolean
# bb=True
# print(type(bb))
# # True or False

# # 형변환
# # string_number = "3"
# # print(string_number + 5)

# # 문자열 출력
# name = "박지훈"
# age = 4
# # 퀴즈
# # 제 이름은 최민호이고, 4살 입니다.

# print("제 이름은 %s이고, %d살 입니다." %(name, age)) 
# print("제 이름은 {0}이고, {1}살 입니다.".format(name,age))
# print(f"제 이름은 {name}이고, {age}살 입니다.")

# # 리스트
# my_list = ['java', 'python', 'django', 'c++', 'HTML']
# print(my_list[2])
# my_list[0] = "CSS"
# print(my_list[0])

# print(*my_list)  # list 전체 출력

# print(len(my_list))  # list 안에 있는 변수의 개수

# print(*my_list[1:4])  # 인덱싱, 슬라이싱

# # 연습문제
# # food라는 리스트를 선언하면서 어제 먹은 음식들로 채워진 리스트를 만들어보기

# food = ["새우덮밥", "짬뽕", "밥", "김치", "단무지"]

# print(food[0])
# food[1] = "초밥"

# print(*food)

# for i in range(3):
#     print(food[i], end=" ")

# for i in food:
#     print(i, end = " ")

# 딕셔너리

# dict={"이름":"박지훈", "나이":28, "성별":"남자"}    #해쉬 라는 형식과 유사함
# # KEY : VALUE로 이루어짐

# print(dict['성별'])
# dict["나이"]=40
# print(dict)
# print(type(dict))
# dict["박지훈"]="아무개"
# print(dict)         # dictionary가 아주 중요

# 퀴즈
# 자신의 이름("name") 나이("age") 인사말("msg")로 구성된
# 1. my_info 라는 딕셔너리를 만들기
# 2. my_info 딕셔너리에서 나이만 출력해 보기

# my_info = {"name":"박지훈", "age":28, "msg":"안녕하세요"}
# print(my_info["age"])

# phone_number={
#     "최":"010",
#     "민":"9353",
#     "호":"6698",
#     "studyterm":{'stcamp':'3days',
#                  'python':'2weeks',
#                  'algorithm':'6weeks'},
#     111:'굳굳'}

# print(phone_number["studyterm"]['python'])

# movie = {
#     'movieInfo': {
#         'movieNm': '광해, 왕이 된 남자',
#         'movieNmEn': 'Masquerade',
#         'showTm': '131',
#         'prdtYear': '2012',
#         'openDt': '20120913',
#         'typeNm': '장편',
#         'nations': [{'nationNm': '한국'}],
#         'genres': [{'genreNm': '사극'}, {'genreNm': '드라마'}],
#         'directors': [{'peopleNm': '추창민', 'peopleNmEn': 'CHOO Chang-min'}],
#         'actors': [
#             {'peopleNm': '이병헌', 'peopleNmEn': 'LEE Byung-hun', 'cast': '광해/하선'},
#             {'peopleNm': '류승룡', 'peopleNmEn': 'RYU Seung-ryong', 'cast': '허균'},
#             {'peopleNm': '한효주', 'peopleNmEn': 'HAN Hyo-joo', 'cast': '중전'},
#         ],
#     }
# }

# 1. 영화의 제목 출력
# 2. 다음 영화 감독의 영어 이름을 출력
# 3. 다음 영화의 배우의 인원을 출력하시오

# print(movie["movieInfo"]["movieNm"])
# print(movie["movieInfo"]['directors'][0]["peopleNmEn"])
# print(len(movie["movieInfo"]['actors']))

# 조건문

# a = int(input())
# if a > 3:
#     print("오삼")
# if a < 1:
#     print("냉면")
# elif a > 5:         # 바로 위의 조건이 거짓이고 내 조건이 참이면 실행
#     print("불고기")
# else:               # 바로 위의 조건이 거짓이면 실행
#     print("만세")

# % 나누고난 후의 나머지를 의미 1. 홀수짝수 2. 어떤수의 배수인지 확인할때 사용

# a = int(input())

# 입력받은 숫자가 홀수인지 짝수인지

# if a % 2 == 0:
#     print("짝수")
# else:
#     print("홀수")

# 반복문 while for

# while 조건:
#     실행할 코드
    
#     조건이 참인 동안에 while문 안에있는 코드가 실행된다.

# x = 0
# while x < 10:
#     print("*")
#     x += 1              # 무한 루프를 돌려 결과값을 얻을때 주로 사용

# for i in range(10):
#     print("*")          # 정해진 횟수가 있을 때 많이 사용

# numbers = [1,2,3,4,5,6,7,8,9]

# for i in numbers:
#     if i % 2 == 0:
#         pass
#     else:
#         print("%d는 홀수입니다."%i)

# while numbers[i] < 10:
#     if numbers[i] % 2 == 1:
#         print(f"{numbers[i]}는 홀수입니다.")
#         i += 1

# 함수 : 반복하거나 자주 사용하는 코드를 묶어놓은 덩어리

# def abc():
#     print(" ()  ()  ")
#     print(" ()  ()  ")

# 모듈 : 여러가지를 짬뽕시켜서 실행시키는 뭉태기

import random
menu = ['인생설렁탕', '홍콩반점', '빽다방', '국대짬', "버거킹", "김밥천국"]
select_lunch = random.choice(menu)
select_lunch = random.choices(menu, k = 2)  # 랜덤하게 여러개 뽑는데 중복이 가능
select_lunch = random.sample(menu, k = 3)
print(select_lunch)