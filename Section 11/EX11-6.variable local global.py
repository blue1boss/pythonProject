'''
지역변수(local)
    함수 내부에 선언
    함수 내부에서만 사용이 가능한 변수
    함수 종료시에 같이 소멸된다


전역변수(globl)
    함수 외부선언
    함수 내부 외부 모두 가능하다.
'''

gVar= '전역' #
def globalAndLocal():
    lVar='지역' #아래 함수 안에서만 사용이 가능하다
    print(f'{gVar} 변수입니다') #전역변수 참조만 한다.
    print(f'{lVar} 변수입니다') #

def gloablAndLocal2():
    lVar ='지역2'
    print(f'{gVar} 변수입니다')
    print(f'{lVar} 변수입니다')

globalAndLocal()
globalAndLocal2()