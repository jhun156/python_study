# 객체지향 프로그래밍 OOP (Object Oriented Programing)

# class Calculator():
#     numberofcalcul = 0

#     def __init__(self):
#         self.result=0
#         Calculator.numberofcalcul += 1

#     def getsum(self,value):
#         self.result += value
#         return self.result
    
# cal1=Calculator()
# print(cal1.numberofcalcul)

# cal1.getsum(3)
# cal1.getsum(4)
# cal1.getsum(5)

# cal2=Calculator()
# print(cal2.numberofcalcul)

# cal1.numberofcalcul = 20
# Calculator.numberofcalcul = 10
# print(cal1.numberofcalcul)
# print(cal2.numberofcalcul)

# class PlusMinus:
    
#     # def data(self,first,second):
#     #     self.first = first
#     #     self.second = second

#     def __init__(self,first,second):
#         self.first = first
#         self.second = second

#     def plus(self):
#         result = self.first + self.second
#         return result
    
#     def minus(self):
#         result = self.first - self.second
#         return result
    
# a=PlusMinus(3,5)
# b=PlusMinus(4,6)
# print(a.first,b.first)
# print(a.plus())
# print(a.minus())


# del kia      
# class Car:
#     def __init__(self,name,price):
#         self.name = name
#         self.price = price

#     def __add__(self,another):
#         return self.price + another.price
    
#     def __str__(self):
#         return f"{self.name}의 가격은 {self.price}입니다"
    
# kia = Car('k8', 300)
# bmw = Car('m5', 500)
# print(kia+bmw)

# print(kia)  # 인스턴스 삭제


# def deco(func):
#     def wrapping(value):
#         print("우유빛깔")
#         func(value)
#         print("화이팅")
#     return wrapping

# @deco
# def call_name(name):
#     print(name)

# @deco
# def call_age(age):
#     print(age)

# call_name("나나")
# call_age(15)

# class Car:
#     def __init__(self,name,price):
#         self.name=name
#         self.price=price
    
#     @staticmethod
#     def add_price(one,another):
#         print(one+another)

# kia = Car('k8', 300)
# bmw = Car('m5', 500)

# Car.add_price(500,700)                  # class로 접근할 것! (인스턴스 접근도 가능하나 안하는 것이 국룰임)

class Make_Pies:
    cnt = 0
    def __init__(self,name,age):
        self.name=name
        self.age=age
        Make_Pies.cnt += 1

    @classmethod
    def number_of_pies(cls):
        print(f'파이를 {cls.cnt}명이 만들고 있습니다.')

a = Make_Pies('kevin',40)
b = Make_Pies('jane',35)
Make_Pies.number_of_pies()