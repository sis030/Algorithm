# 6055

# 2개의 정수값이 입력될 때,
# 그 불 값이 하나라도 True 일 때에만 True 를 출력하는 프로그램을 작성해보자.

# 출력
a,b=input().split()
print(bool(int(a)) or bool(int(b)))