# 6054

# 2개의 정수값이 입력될 때,
# 그 불 값이 모두 True 일 때에만 True 를 출력하는 프로그램을 작성해보자.

# 출력(내 코드)
a, b = map(int,input().split())

if bool(a) and bool(b) == True:
    print('True')
else:
    print('False')

# 출력(권장 코드)
a,b=input().split()
print(bool(int(a)) and bool(int(b)))

