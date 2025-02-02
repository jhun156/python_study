a = input("문자 입력: ")  # 문자 입력받기
A = ord(a)  # 입력받은 문자부터 시작

arr = [[' ' for _ in range(3)] for _ in range(3)]  # 3x3 배열 초기화

j = 0  # 열 인덱스
while j < 3:
    i = 2 - j  # 각 열에서 채우기 시작할 위치 조정 (아래 → 위)
    while i < 3:
        arr[i][j] = chr(A)  # 문자 채우기
        A += 1
        i += 1  # 위로 이동
    j += 1  # 다음 열로 이동

# 🔥 결과 출력
for row in arr:
    print(' '.join(row).rstrip())  # 불필요한 공백 제거
