n,m = map(int,input().split()) #행렬 크기 n,m 입력받음

a,b=[],[] #행렬을 담을 리스트 a와 b 초기화

for i in range(n):
    a.append(list(map(int,input().split()))) #n번 동안 리스트 a에 행렬값 입력 받음
    
for i in range(n):
    b.append(list(map(int,input().split()))) #n번 동안 리스트 b에 행렬값 입력 받음
    
for i in range(n):
    for j in range(m):  #행렬이 반복될 동안
        print(a[i][j]+b[i][j], end=" ") #a,b 더한 값을 출력
    print() #각 행이 끝나면 줄바꿈
    