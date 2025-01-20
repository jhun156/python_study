# 내 풀이

a = str(input())

print(ord('A'))
print(ord('Z'))
print(ord('a'))
print(ord('z'))

if ord(a) >= 65 and ord(a) <= 90:
    print("대문자입니다")
elif ord(a) >=97 and ord(a) <= 122:
    print("소문자입니다.")

# gpt 풀이

a = input()

if a.isupper():
    print("대문자입니다")
elif a.islower():
    print("소문자입니다.")