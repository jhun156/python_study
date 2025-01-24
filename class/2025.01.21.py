# swap

y,x = 1,5
y,x = x,y

tmp = y
y = x
x = tmp

a,b = 0,-1
a,b = bool(a),bool(b)
print(a,b)  #False, True

# 소수 float

a = 3.14
print(type(a))  #float
print(round(a),1)   #소수점 1자리까지만 나온다. 2번째에서 반올림해서 출력 3.1
print(f'{a:.1f}')

a = 3.15

print(round(a,1))   # 부동소숫점을 이용을 해서 실수를 근사값으로 표현

a = 1.2 - 1.1   # floating point error 부동소숫점 오류
print(a)    # 0.099999999987

# Decimal module은 정확한 대신 무겁고 느림
# round = 반올림 ceil = 올림 floor = 내림

print(round(0.4))
print(round(1.4))
print(round(2.4))
print(round(3.4))
print(round(4.4))
print(round(5.4))


print(round(0.6))
print(round(1.6))
print(round(2.6))
print(round(3.6))
print(round(4.6))
print(round(5.6))


print(round(0.5))
print(round(1.5))
print(round(2.5))
print(round(3.5))
print(round(4.5))
print(round(5.5))

# 앞의 수가 짝수면 내림, 앞의 수가 홀수면 올림 (오사오입)

print(round(0.15+0.00001,1))
print(round(0.25+0.00001,1))
print(round(0.35+0.00001,1))
print(round(0.45+0.00001,1))
print(round(0.55+0.00001,1))
print(round(0.65+0.00001,1))

# 우리가 파이썬에서 소수점을 표현할때 decimal이란 모듈이 무겁고 느리다
# 그래서 round를 사용한다.
# 그런데 round도 부동소수점 에러 때문에 제대로 작동이 안된다.
# 그럼 how?
# 계산하려는 값에 아주 작은 수를 더한후 round() 메서드를 사용하면 정확함.

a = 3.12523
b = 2.72395
# 소수 2번째자리까지
# 두 실수를 반올림해서 정수 표현하기

print(round(a+0.002,2),round(b,2))
print(round(a),round(b))
from math import floor
print(floor(a+0.5))
print(floor(a+0.5))

# 순서라는 개념이 있는 자료형
# str, list, tuple, range

print('오늘의 컨디션은 "100" 입니다')

# 문자열 slicing

s = 'abcdefg'

print(s + '1')

# list

list = [1,2,3,4]

s = 'abcdefg'
ret = s.replace(s[1],'K')
print(ret)

count = 0
for i in list:
    count += 1
print(count)

print(list*3)
print(list+[7,8,9])

lst = [1,2,3,4,[5,6,7],8]
print(lst[4][0])    #5
print(lst[-2][-3])  #5

# tuple

tp = (1,2,3,4,5)
print(tp)
print(type(tp))
print(tp[1])
print(len(tp))
print(tp[-1])

# dictionary

# key - value 형태로 저장 (hash)라는 자료구조를 기반으로 만들어진 자료형

# 순서가 없고, 중복이 안된다(같은 키값을 여러번 사용을 못함)

di={1:3,2:{4:5},'학':6,'교':[7,8,9]}
print(di)
print(type(di))
print(di[1])
print(di[2][4])
print(di['학'])
print(di['교'][2])

di[111]=di.pop(1)
print(di)

# set
# 리스트안의 중복을 제거할때 많이 씀
# list = [1,1,2,3,4,4,5,2,3,3,4,3,4,2,2,3,4]

# # list=list(set(list))
# print(list)
# print(set(list))
# print(type(set(list)))
# lst = list(set(list))
# print(lst)

# a,b = 0,-1
# print(bool(a))

# 논리연산자
a = True
b = False
c = True
d = False
print(a and b)
print(a and c)
print(a or b)
print('a' and 'b')  # b
print('' and 'a')   # ''
print(0 and 1)      # 0

print(1 or 0)       # 1
print(0 or -1)      # -1
print(-1 or 1)      # -1

a = 1
b = 0
c = 3
print(a or c)       # 1
print(a|c)          # 3
print(b or c)       # 3
print(a and b)      # 0
print(a and c)      # 3
print(c and a)      # 1

result = 10%3+2**2
print(result)

result2 = -3**2
print(result2)

# 객체를 비교하는 is

a = 2       #int
b = 2.0     #float

if a is not b:
    print('정답')
else:
    print('오답')

# 깊은복사 얕은복사 ~~

a = 5 # 할당한다
b = 5
print(id(a),id(b))
a = 3
print(id(a),id(b))

lst = [1,2,3]
lst2 = list[:]
list[0] = 100
print(lst2[0])

import copy 
lst = [[1,2],[3,4]]
lst2 = copy.deepcopy(lst)
lst[0][0] = 100
print(lst2[0][0])