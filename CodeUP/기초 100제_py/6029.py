# 6029

# 16진수를 입력받아 8진수(octal)로 출력해보자.

# 출력
a=input() #수 입력받음
a=int(a, 16) #입력받은 수를 16진수로 해석해서 10진수로 변환
print("%o" % a) #10진수를 8진수 형태로 출력

#문자열 진법 변환 
# int(a,2) 입력받은 a를 2진수로 해석해서 10진수 변환
# int(a,8) 입력받은 수를 8진수로 해석해서 10진수 변환
# int(a,16) 입력받은 수를 16진수로 해석해서 10진수 변환