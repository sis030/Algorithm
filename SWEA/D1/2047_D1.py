s = input().split('_')

result = [i.upper() for i in s]
print("_".join(result))

#원래 내가 작성한 코드
s=input().split('_')

for i in s:
    if i.islower():
        print(i.upper(), end="_")
    else:
        print(i.upper(), end="_")
#야매로 했는데 이렇게 하니까 마지막에도 _가 출력되어서 위에 코드로 수정함