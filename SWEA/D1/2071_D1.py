T = int(input())

for test_case in range(1, T + 1):
    n=map(int,input().split())
    total=0
    for i in n:
        total+=i
    average = total / 10
    print(f'#{test_case} {round(average)}')


# 코드 보완점 => sum()으로 코드 간소화
T = int(input())

for test_case in range(1, T + 1):
    numbers = list(map(int, input().split()))
    average = sum(numbers) / 10
    print(f'#{test_case} {round(average)}')
