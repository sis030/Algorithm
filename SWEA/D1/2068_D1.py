T = int(input())

for test_case in range(1, T + 1):
    n = list(map(int,input().split()))
    print(f'#{test_case} {max(n)}')

#코드 보완점 => max()를 쓰지 않고 로직을 짤 수 있어야 함
T = int(input())

for test_case in range(1, T + 1):
    n = list(map(int, input().split()))
    max_num = n[0]  # 첫 번째 숫자를 초기 최대값으로 설정
    for num in n:   # 리스트를 순회하며
        if num > max_num:  # 현재 숫자가 최대값보다 크면
            max_num = num  # 최대값을 갱신
    print(f'#{test_case} {max_num}')