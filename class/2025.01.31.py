'''
# set, dictionary 관련 메소드
# set (중복을 허용하지 않는 데이터들의 묶음)

# 값 추가
# s = {1,2,3,4,5}
# s.add(6)                    # 하나만 추가
# s.update([11,12,13,14])     # 여러개 동시에 추가
# print(s)                    # {1, 2, 3, 4, 5, 6, 11, 12, 13, 14}

# # 값 삭제
# s.remove(6)                 # 하나만 삭제, 없는 값을 삭제하려 하면 오류발생
# print(s)
# s.discard(16)
# print(s)                    # 하나만 삭제, 없는 값을 삭제해도 오류 발생하지 않음

# s.clear()                   # 원소 비우기
# print(s)

# 집합 표현

s1 = {1,2,3,4,5}
s2 = {2,4,6,8}

print(s1&s2)                        # 교집합
print(s1.intersection(s2))          # 교집합

print(s1|s2)                        # 합집합
print(s1.union(s2))                 # 합집합

print(s1-s2)                        # 차집합
print(s1.difference(s2))            # 차집합

# 부분집합  <True or False>
print(s1<=s2)
print(s1.issubset(s2))

# s1이 s2의 모든 항목을 포함하고 있다면 True 반환
print(s1>=s2)
print(s1.issuperset(s2))
'''

'''
st =  { 'kevin' : 1, 'john' : 2, 'bob' : [3,4,5]}
# 딕셔너리 값(value) 출력
# print(st['kevin'])     # 없는 값을 출력하려고 하면 key error 발생
# print(st.get('kevin11','없는key입니다.'))   # .get('key',default 값) 오류가 발생하지 않아서 추천하심

# 딕셔너리에 값 추가하기
# 방법 1 : 직접 key를 입력하는 방법

st['kate'] = 'hi'       # 없는 key를 입력하면 자연스럽게 추가됨
print(st)
st['kevin'] = 11        # 있는 key를 입력하면 값이 바뀜
print(st)

# 방법 2 : update() 메서드 사용하는 방법
st.update(camel=11)
print(st)

st.update(kevin=100)
print(st)

st.update(even=200,faker=300)           # update() 메서드는 동시에 여러개 값을 추가하는 것도 가능함
print(st)

dict2 = {'fly' : 201, 'amy' : 301}
st.update(dict2)
print(st)
'''
'''
연습문제
st =  { 'kevin' : 1, 'john' : 2, 'bob' : [3,4,5]}
ls_key = ['asdf','zcv','qwe']
ls_value = [1,2,3]

첫번째 방법
for i in range(3):
    st[ls_key[i]] = ls_value[i]
print(st) 

두번째 방법
for i in range(3):
  st.update({ls_key[i]:ls_value[i]})
print(st) 

세번째 방법
temp = dict(zip(ls_key,ls_value))
st.update(temp)
print(st) 

네번째 방법
for i in range(3):
    st.setdefault(ls_key[i],ls_value[i])              # 원본 데이터가 있다면 setdefault 를 써도 기존 데이터가 보존이 된다.
print(st)

st =  { 'kevin' : 1, 'john' : 2, 'bob' : [3,4,5]}
st.setdefault('amy','korea')
print(st)
st.setdefault('kevin',1000)
print(st)
'''
'''
# 삭제
st =  { 'kevin' : 1, 'john' : 2, 'bob' : [3,4,5]}
del st['kevin']         # 없는 값을 삭제하려하면 key error 발생, 반환값 x
print(st)

st.pop('kevin11','없음')        # 없는 경우에 default 값을 작성해주면 key error 발생하지 않음, 반환값 o
print(st)

st =  { 'kevin' : 1, 'john' : 2, 'bob' : [3,4,5]}

lst = st.keys()
print(lst)
print(list(lst))

lst = st.values()
print(lst)
print(list(lst))

lst = st.items()            # 튜플의 형태로 묶여서 반환함
print(lst)
print(list(lst))
'''

# collection 모듈에서 counter 라는 클래스 이용하기
from collections import Counter

lst = ['apple','mango','banana','mango','apple','mango','banana','mango','apple']

print(Counter(lst))
ret = dict(Counter(lst))
print(ret)

print(Counter('an applemango'))
st = 'an applemango'
# st에서 가장 많이 사용된 알파벳 출력
ret = dict(Counter(st))
ret=sorted(ret.items(),key=lambda x:x[1], reverse = True)
print(ret[0][0])

st = 'an applemango'
ret=Counter(st).most_common(1)
print(ret[0][0])

a = Counter('apple')
b = Counter('mango')
print(a+b)
print(a-b)