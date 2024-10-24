num=list(range(1,31))

for i in range(28):
    num.remove(int(input())) #30명 번호 있는 리스트에 28명의 학생 번호를 입력해서 제거하면 제출안한 2명의 번호만 남음

for i in num:
    print(i)