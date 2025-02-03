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

class PlusMinus:
    
    # def data(self,first,second):
    #     self.first = first
    #     self.second = second

    def __init__(self,first,second):
        self.first = first
        self.second = second

    def plus(self):
        result = self.first + self.second
        return result
    
    def minus(self):
        result = self.first - self.second
        return result
    
a=PlusMinus(3,5)
b=PlusMinus(4,6)
print(a.first,b.first)
print(a.plus())
print(a.minus())

class Car:
    def __init__(self,name,price):
        self.name = name
        self.price = price

    def __add__(self,another):
        return self.price + another.price
    
    def __str__(self):
        return f"{self.name}의 가격은 {self.price}입니다"
    
kia = Car('k8', 300)
bmw = Car('m5', 500)
print(kia+bmw)

print(kia)

del kia         # 인스턴스 삭제