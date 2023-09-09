gVar = '전역'

def globalAndLocal():
    lVar= '지역'
    gVar= '변경된 전역이 아닌 새로운 지역'
    print(f'{gVar} 변수 입니다.')
    print(f'{lVar} 변수 입니다.')

globalAndLocal()
#값을 대입하는 순간 지역변수가 되는 것이다.
print(gVar)
#그대로 '전역'으로 나오므로 값 대입을 해도 값이 변하지 않는 것을 볼 수 있다.