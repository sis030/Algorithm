# 6044

# 정수 2개(a, b)를 입력받아 합, 차, 곱, 몫, 나머지, 나눈 값을 자동으로 계산해보자.
# 단, b는 0이 아니다.

# 출력
a,b=map(int, input().split())
print(f'{a+b}\n{a-b}\n{a*b}\n{a//b}\n{a%b}\n{a/b:.2f}')

#소수점 출력 형식 지정(참고 예시)
# format() : "{:.nf}".format(변수/값)
# f-string : f"{변수/값:.nf}"

