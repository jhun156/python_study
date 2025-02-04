string = input()

def max_index(str):
    a = ord(str[0])
    result = 0
    for i in range(len(str)):
        if a < ord(str[i]):
            a = ord(str[i])
            result = i
    return result

def min_index(str):
    a = ord(str[0])
    result = 0
    for i in range(len(str)):
        if a > ord(str[i]):
            a = ord(str[i])
            result = i
    return result

print(max_index(string))
print(min_index(string))