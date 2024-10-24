n,m = map(int, input().split())
result = n-m

if result > 0:
    print(result)
else:
    result *= -1
    print(result)