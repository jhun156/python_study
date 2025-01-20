# 내 풀이

a,b,c = map(int,input().split())

if a >= b and a >= c:
    if b >= c:
        print(f"MAX={a}")
        print(f"MIN={c}")
    else:
        print(f"MAX={a}")
        print(f"MIN={b}")
elif b >= a and b >= c:
    if a >= c:
        print(f"MAX={b}")
        print(f"MIN={c}")
    else:
        print(f"MAX={b}")
        print(f"MIN={a}")
else:
    if a >= b:
        print(f"MAX={c}")
        print(f"MIN={b}")
    else:
        print(f"MAX={c}")
        print(f"MIN={a}")

# gtp 풀이

a, b, c = map(int, input().split())

# 최대값과 최소값 계산
max_value = max(a, b, c)
min_value = min(a, b, c)

# 결과 출력
print(f"MAX={max_value}")
print(f"MIN={min_value}")