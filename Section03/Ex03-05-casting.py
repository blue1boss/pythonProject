'''
형변환(casting)
    변수에 유형을 지정하려는 경우 캐스팅으로 가능.
'''
#정수형
x=int(1)
print(x)
y=int(2.8)
print(y)
z=int("3")
z2='3'
print(z)
print(x+z)
print(str(x)+z2)
print(x+int(z2))

#실수형
x=float(1)
print(x)
z=float('3')
print(z)

#문자형
x=str(1) #'1'
y=str(2) #'2'
print(x+y) #문자열+ 문자열 = 문자연결

#아스키코드 변환
a=ord('A')
print(a)
b=chr(65)
print(b)

#4
#대입 연잔사 : 변수에 값을 저장하기 위해 사용하는 연산자
'''
print 형식문자
%d: 정수 데이터
%f: 실수 데이터 
%o: 8진수 데이터 
%x: 16진수 데이터 
%s: 문자열 데이터 
%c: 문자 하나 데이터
'''
a,b= 10,20
print('a=%d,b=%d' %(a,b))

a,b= b,a
print('a=%d,b=%d' %(a,b))

'''
tmp=a
a=b
b=tmp
서로 값 바꾸는 방식 '''

'''
복합 대입연산자 
    +=
        ex) x +=3 -> x = x+3과 같은 말이다 
    -=
        ex) x-= 3 -> x = x-3과 같은 말이다 
'''
piggy_bank=0
money = 10000
piggy_bank += money #piggy bank = piggy bank + money
print(f'저금통에 용돈 {money}원을 넣었습니다.')
print(f'지금 저금통에는 {piggy_bank}원이 있습니다.')

snack = 2000
piggy_bank -= snack # piggy bank = piggy bank -2000
print(f'저금통에서 스택 구입비 {snack}원을 뺏습니다.')
print(f'지금 저금통에는 {piggy_bank}원이 있습니다.')