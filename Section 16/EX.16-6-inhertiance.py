'''
죽음의 다이아몬드
'''

class A:
    def greeting(self):
        print('안녕하세요 A입니다')

class B(A):
    def greeting(self): #오버라이딩  - 부모 클래스 메서드 재정의
        print('안녕하세요,B입니다')


class C(A): #A호출하는 기능
    def greeting(self):
        print('안녕하세요,C입니다')

class D(B,C):
    pass #내부동작 필요하지 않고, 빈껍데기만 필요할 경우에 사용하는 명령어

#실행코드
x= D()
x.greeting() # 안녕하세요,B입니다.
print(D.mro()) #상속에서의 우선순위 정해지는 것 mro() 다중 상속시에 메서드 호출 순서를 알 수 있게 해준다.
