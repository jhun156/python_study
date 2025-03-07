'''
# 진법 바꾸기

a = 13
b = bin(a)
c = oct(a)
d = hex(a)
print(a,b,c,d)
print(type(b))
print(int(b,2))
print(int(c,8))
print(int(d,16))
'''

'''
n = [1,1,1]
ans = 0
for i in range(3):
    ans += n[i] * (3 ** (2-i))

print(ans)

a = 18

def trans(value):

    ans = ''
    while value >= 1:
        value,rest = divmod(value,3)
        ans += str(rest)
    ans = ans[::-1]
    return ans

ret = trans(a)
print(ret)

print(int(ret,3))   # 3진수를 10진수로 바꿔서 출력
'''

'''
# 비트연산자
print(13&9)     # ampersand 둘다 1이면 참
print(13|9)     # bar       둘중 하나만 1이면 참
print(13^9)     # caret     두개가 같으면 0, 두개가 다르면 1

print(14^9)
print(10<<2)
print(10>>2)

# 부분집합 구하는 방법, 비트연산자
arr=[1,2,3]
n=3

for i in range(1<<3):
    answer=[]
    for index in range(3):
        if i&(1<<index)!=0:
            answer.append(arr[index])
    if answer:
        print(answer)
'''
'''
# GCD : 최대공약수 greatest common divisor

ans = 0
a,b = map(int,input().split())
for i in range(2,min(a,b)):
    if a % i == 0 and b % i == 0:
        ans = i
'''
'''
# 유클리드 호제법
# 최대공약수
ans = 0
a,b = map(int,input().split())
while b:
    ans = a % b
    a = b
    b = ans
print(a)

# LCM 최소공배수 least common multiflial
#
# LCM = gcd x ( a / gcd ) x ( b / gcd )
'''

'''
# prime number 소수 구하기
# 에라토스테네스의 체

a=int(input())   # N값 입력
ans=[]
for i in range(2,a+1): # 2~N까지 다 확인하기
    flag=0
    for j in range(2,i): # 2부터 i보다 작은수로 나눠지는 확인할 수
        if i%j==0: # 나눠 진다면
            flag=1 # 소수가 아님
            break
    if flag==0: ans.append(i) # break 안걸린 친구들은 소수임!
print(ans)

a = int(input())
check = [0] * (a + 1)
end = int(a ** 0.5)

for i in range(2, end + 1):  # 1. 2부터 입력받은 수 까지 확인
    if check[i] == 1: continue  # 4. 이미 체크가 된 값이라면 pass
    for j in range(i + i, a + 1, i):  # 2. 작은수부터 배수에 해당하는 인덱스에
        check[j] = 1  # 3. 1 체크하기

# 5. 소수 출력하기
for i in range(2, a + 1):
    if check[i] == 0: print(i, end=' ')
'''

'''
# Sliding Window

# M 개의 정수를 입력
# 연속된 n개의 정수의 합이 최대일 때 그 구간은 언제인지 or 구간합은 뭔지

n, m = map(int,input().split())
arr = list(map(int,input().split()))

Max = 0
for i in range(m):
    Max += arr[i]

cnt = 0
top = m

while cnt < n-m:

    tmp = Max
    tmp += arr[top]
    tmp -= arr[cnt]
    Max = max(tmp,Max)
    top += 1
    cnt += 1

print(Max)
'''

'''
n,m=map(int,input().split())
arr=list(map(int,input().split()))
Sum=0
for i in range(m):  #첫 m개 구간의 합 구하기
    Sum+=arr[i]
    
Max=Sum
for i in range(n-m):
    Sum+=arr[i+m] # 오른쪽값 더하고
    Sum-=arr[i] # 왼쪽값 빼기
    if Sum>Max: Max=Sum # 맥스값 갱신
print(Max)
'''