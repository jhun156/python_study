a = input()

arr1 = [i for i in range(ord(a),ord(a)+5)]
arr2 = [i for i in range(ord(a),ord(a)-5,-1)]

for i in arr1:
    print(chr(i),end='')

print()

for i in arr2:
    print(chr(i),end='')
