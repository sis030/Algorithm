T=int(input())

for test_case in range(1, T+1):
    n=list(map(int,input().split()))
    n.sort()
    num_list=n[1:9]
    result=sum(num_list)/len(num_list)
    print(f'#{test_case} {round(result)}')

#다른 풀이 (1) : 굳이 범위 지정 없이 max(),min() 해주고 구하는 방법

# 다른 풀이 (2) : 리스트에서 최솟값과 최대값을 pop해서 없애주고 계산하는 방법