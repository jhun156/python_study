def main():
    
    a = int(input())
    num = 0

    while num != 1:
        if a < 20:
            print("더 큰수를 입력하세요")
            a = int(input())
        elif a > 20:
            print("더 작은수를 입력하세요")
            a = int(input())
        else:
            print("정답입니다")
            num = 1
            break

main() * 4

