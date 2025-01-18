# def add(a,b):   # a, b는 매개변수(parameter)
#     result = a + b
#     return result

# print(add(1,2)) # 1, 2는 인수(arguments)

# def say():
#     return "Hi"

# print(say())

# def add(a, b):
#     print("%d, %d의 합은 %d입니다." %(a, b, a+b))

# a = add(1,2)

# print(a)

# def say():
#     print('hi')

# a = say() 

# print(a)

# def sub(a,b):
#     return a - b

# a = sub(3,1)

# print(a)

# 여러개의 인수를 받을때
# def add_many(*args):
#     result = 0
#     for i in args:
#         result += i
#     return result

# a = add_many(1,2,3,4,5)

# print(a)

# def add_mul(choice, *args):
#     if choice == "add":
#         result = 0
#         for i in args:
#             result += i
#     elif choice == "mul":
#         result = 1
#         for i in args:
#             result *= i
#     return result

# a = add_mul("add", 1,2,3,4,5)
# b = add_mul("mul", 1,2,3,4,5)

# print(a)
# print(b)

# def print_kwargs(**kwargs):
#     print(kwargs)

# print_kwargs(a=1,b=2,c=3)

# def add_and_mul(a,b):
#     return a+b, a*b

# a,b = add_and_mul(3,4)

# print(a)
# print(b)

#함수에서 리턴값은 1개이다.

# def say_nick(nick):
#     if nick == "바보":
#         return
#     print("나의 별명은 %s입니다." % nick)

# say_nick("바보")

# def say_myself(name, old, man):
#     print("나의 이름은 %s입니다." % name)
#     print("나의 나이는 %s입니다." % old)
#     if man == "man":
#         print("남자입니다.")
#     else:
#         print("여자입니다.")

# say_myself("박지훈", 28, "woman")

# a = 1
# def vartest(a):
#     a = a + 1

# print(vartest(a))

# a = 1
# def vartest(a):
#     a += 1
#     return a

# print(vartest(a))

# a = 1
# def vartest():
#     global a
#     a = a + 1

# vartest()
# print(a) 

# b = [1, 2, 3]
# def vartest2(b):
# b = b.pop()
#     return b

# vartest2(b)
# print(b)

def add(a,b):
    return a + b

add = lambda a, b: a+b
a = add
print(a(3,4))