n = int(input())  #팩토리얼 연산 할 임의의 수를 입력

result = 1 
if n > 0:
    for i in range(1, n+1): #1부터 n+1값까지 반복
        result *= i
print(result)