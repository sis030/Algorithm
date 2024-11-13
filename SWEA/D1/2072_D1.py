T = int(input())

for test_case in range(1, T + 1):
    n=map(int,input().split())
    result = 0
    for i in n:
        if i % 2 != 0:
            result += i
    print('#'+str(test_case), result)