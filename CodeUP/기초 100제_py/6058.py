# 6058

# 2개의 정수값이 입력될 때,
# 그 불 값(True/False) 이 모두 False 일 때에만 True 를 출력하는 프로그램을 작성해보자.

# 출력
a, b = map(int,input().split())

if bool(not a) and bool(not b):
    print("True")
else:
    print("False")