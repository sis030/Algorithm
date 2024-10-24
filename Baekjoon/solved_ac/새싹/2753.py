year=int(input())

if (year%4==0) and (year%100!=0) or (year%400==0):
    print('1')
else:
    print('0')

#윤년 구하기 조건
# 윤년은 4로 나누어떨어지지만 100으로 나누어떨어지지 않는 해이거나, 400으로 나누어떨어지는 해
# (year%4==0) and (year%100!=0) or (year%400==0)