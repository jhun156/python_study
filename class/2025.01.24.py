# st = 'apple,banana,mango'

# index = st.find('z')
# print(index)

# alpha = st.index('p')
# print(alpha)

# # 모두 대문자인지 / 모두 소문자인지
# print(st.isupper())
# print(st.islower())
# print(st.isalpha())

# print(st.count('a'))

# st = ['a','p','p','l','e']
# ret = "".join(st)       # "" - 구분자
# print(ret)

# st = ['apple','banana','mango']
# rnt = ",".join(st)
# print(rnt)

# str2=st.upper()
# print(str2)
# str2=str2.lower()
# print(str2)

# st = '  apple  '
# print(st)
# str2 = st.lstrip()
# print(str2)
# str3 = st.rstrip()
# print(str3)
# str4 = st.strip()
# print(str4)

# str = 'apple'
# str2 = str.replace('ap','mp')
# print(str2)

# st = 'apple'
# print(reversed(st))
# print(list(reversed(st)))

# st2 = "".join(list(reversed(st)))
# print(st2)

# print(st[::-1])

# 리스트 관련 메서드

# st = ['apple','banana','mango']
# st.insert(1,'orange')
# a = st.index('orange')
# print(a)

# str1 = [1,2,3]
# str2 = [4,5]

# str1 += str2

# str1.extend(str2)
# print(str1)

# st = [1,2,3,4,3,5]
# ret = st.pop()
# print(st)
# print(ret)
# st.remove(3)
# print(st)

# del st[2:]
# print(st)

# st = [1,2,3,4,5]
# st.reverse()
# print(st)

# st = st[::-1]
# print

# 정렬 메소드 sort sorted

# a1 = [6,3,9]
# print(a1)

# 오름차순으로 정렬 sort = 원본데이터를 정렬, sorted = 정렬된 데이터를 반환

# a1.sort()
# print(a1)

# 내림차순으로 정렬
# a1.sort(reverse=True)
# print(a1)

# sorted 사용
# ret=sorted(a1)
# print(a1)
# print(ret)
# ret=sorted(a1,reverse=True)
# print(ret)

# a1 = 'asdf'
# a1.sort()
# print(a1)
# a2 = sorted(a1)
# print(a2)
# a2 = "".join(a2)
# print(a2)

lst=list(range(1,11))

# print(lst)
# lst2 = sorted(lst,reverse=True)
# print(lst2)

ret=sorted(lst,key=lambda x:-x)
print(ret)

# 1. 홀수우선
# 2. 내림차순

# sorted()
# lst -> iterable 객체
# key = -> 정렬을 할 기준
# reverse=True -> 내림차순옵션
# 문자열은 lambda의 리턴값으로 음수 불가!!

# lst = ['apple','mango','banana','mandu']

# lst.sort()
# print(lst)

# ret=sorted(lst,reverse=True)
# print(ret)
# ret2=sorted(lst,key=lambda x:-x)    # 문자열의 경우 reverse=True 를 이용해야 가능
# ret2=sorted(lst,key=lambda x : x, reverse = True)

# lst = [(3,'banana'),(2,'apple'),(1,'carrot')]

# 결과 = [(2,'apple'),(3,'banana'),(1,'carrot')]

# ret = sorted(lst,key=lambda x:x[1],reverse = True)
# print(ret)

