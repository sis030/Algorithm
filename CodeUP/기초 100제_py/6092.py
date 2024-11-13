# 6092

# 정보 선생님은 수업을 시작하기 전에 이상한 출석을 부른다.

# 선생님은 출석부를 보고 번호를 부르는데,
# 학생들의 얼굴과 이름을 빨리 익히기 위해 번호를 무작위(랜덤)으로 부른다.

# 그리고 얼굴과 이름이 잘 기억되지 않는 학생들은 번호를 여러 번 불러
# 이름과 얼굴을 빨리 익히려고 하는 것이다.

# 출석 번호를 n번 무작위로 불렀을 때, 각 번호(1 ~ 23)가 불린 횟수를 각각 출력해보자.

# 출력
n = int(input())  #출석 번호 부른 횟수 n
c = input().split()  #무작위로 부른 번호 c개

for i in range(n):  #n번 반복될 동안
    c[i] = int(c[i]) #c의 요소들을 정수형으로 전환

r=[] #결과값을 담을 빈 리스트 생성
for i in range(24):  #23번 반복
    r.append(0) #리스트 r에 0 추가

for i in range(n): #n번 반복될 동안
    r[c[i]] += 1 #리스트 c의 요소들을 카운트 해서 리스트 r에 저장

for i in range(1,24): #23까지 반복
    print(r[i], end=" ") #카운팅 된 횟수를 공백으로 구분하여 한 줄 출력


#다른 분이 푼 좀 더 좋아보이는 코드(참고하기)
stlist = list()

for i in range(24):
    stlist.append(0)
    
num = int(input())
numlist = input().split()

for i in range(num):
    stlist[int(numlist[i])] += 1
    
for i in range(1, len(stlist)):
    print(stlist[i], end=' ')