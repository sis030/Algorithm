# 6073

# 정수(1 ~ 100) 1개가 입력되었을 때 카운트다운을 출력해보자.

# 출력
n=int(input())

while True:
    n -= 1
    print(n)
    
    if n == 0:
        break