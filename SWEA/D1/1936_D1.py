#내가 작성한 코드
a,b=map(int,input().split())

if a>b:
    print('A')
elif a<b:
    print('B')
# 이렇게 하면 1, 2, 3 이외의 수가 들어와도 A와 B를 출력해버림
# 구체적으로 작성해야됨

#다른 코드
a, b = map(int, input().split())
game= [3, 1, 2]
if game[a] == b:
    print('A')
else:
    print('B')
#a의 인덱스가 b의 값과 같을 때 결과 출력하는 코드
