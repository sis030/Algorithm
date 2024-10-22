# 6020

# 주민번호는 다음과 같이 구성된다.
# XXXXXX-XXXXXXX

# 출력
a,b=input().split('-')
print(a+b)

#split()은 특정 구분자를 기준으로 문자열을 나누기만 하고 결과 출력에는 포함되지 않음
#예를 들어 a,b=input().split(':') 하면 a와 b를 :로 구분만 하고 출력은 안함