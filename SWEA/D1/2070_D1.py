T = int(input())

for test_case in range(1, T + 1):
    n,m=map(int,input().split())
    result=0
    if n<m:
        result='<'
    elif n == m:
        result='='
    elif n>m:
        result='>'
    print(f'#{test_case} {result}')


#코드 보완점 1 => result를 굳이 초기화 해서 사용하지 않아도 됨
T = int(input())

for test_case in range(1, T + 1):
    n,m=map(int,input().split())
    if n < m:
        print(f'#{test_case} <')
    elif n == m:
        print(f'#{test_case} =')
    else:
        print(f'#{test_case} >')
# 변수 초기화는 누적 합을 저장할 변수나 재사용 해야 될 경우 꼭 초기화 해둬야 쓰레기 값이 안들어가지만 간단한 코드 작성에서는 안 써도 괜찮음

# 코드 보완점 2 => 함수 처리 하는 습관을 들이면 좋을듯
def compare_numbers(n, m):
    if n < m:
        return '<'
    elif n == m:
        return '='
    else:
        return '>'

T = int(input())
for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    result = compare_numbers(n, m)
    print(f'#{test_case} {result}')

