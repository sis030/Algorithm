# 6045

# 정수 3개를 입력받아 합과 평균을 출력해보자.

# 출력
a,b,c = map(int, input().split())
sum=a+b+c
print(sum,'{:.2f}'.format(sum/3))