# 6056

# 2개의 정수값이 입력될 때,
# 그 불 값(True/False) 이 서로 다를 때에만 True 를 출력하는 프로그램을 작성해보자.

# 출력(내가 작성한 코드)
a,b=map(int,input().split())

if bool(a) != bool(b):
    print('True')
else:
    print('False')


