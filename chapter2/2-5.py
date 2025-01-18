# dic = {'name': 'pey', 'phone': '010-9999-1234', 'birth': '1118'}

# print(dic)

# a = {1:'a'}
# a[2] = [1, 2, 3]

# print(a)


a =  {2: 'b', 'name': 'pey', 3: [1, 2, 3]}

# dictionary의 key는 변형불가능한 자료형을 사용해야하고, 중복되면 안된다. (겹쳐써짐)

print(a.keys())
print(a.values())
print(a.items())
print(a.get('hi',"값이 없습니다"))
print('na' in a)
print('name' in a)

