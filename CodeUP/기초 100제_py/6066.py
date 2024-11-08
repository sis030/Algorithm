# 6066

# 3개의 정수(a, b, c)가 입력되었을 때, 짝(even)/홀(odd)을 출력해보자.

# 출력
a,b,c=map(int,input().split())

if (a % 2 == 0):
    print('even')
else: 
    print('odd')

if (b % 2 == 0):
    print('even')
else: 
    print('odd')

if (c % 2 == 0):
    print('even')
else: 
    print('odd')


#출력(반복문)
a,b,c=map(int,input().split())

for i in [a,b,c]:
    print('even' if i % 2 == 0 else 'odd')