while 1:
    try:
        a,b=map(int,input().split())
        print(a+b)
    except:
        break
        
#입력 조건과 출력 조건이 정해져 있지 않기 때문에
#try와 except를 사용해서 try 후 try 안될 경우 except의 break로 가도록 설계됨