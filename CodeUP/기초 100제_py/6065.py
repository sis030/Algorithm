# 6065

# 3개의 정수(a, b, c)가 입력되었을 때, 짝수만 출력해보자.

# 출력
a,b,c=map(int,input().split())

if (a % 2 == 0):
    print(a)

if (b % 2==0):
    print(b)
        
if(c % 2 == 0):
    print(c)

#출력(반복문)
a,b,c=map(int, input().split())

for i in [a,b,c]:
    if i % 2 == 0:
        print(i)