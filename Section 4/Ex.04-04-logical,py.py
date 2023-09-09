'''
논리 연산자
    관계 연산자와 함꼐 사용되는 연산자로
    2개 이상의 항을 논리적으로 연결할 때 사용한다

    and: 2개 항 모두 True일떄 true
    or: 2개항 어느 쪽 true 일때 true
    not: 논리 값을 반전시킨다.
'''
a= 10
b= 0
print('{}> 0 and {} >0 : {}'.format(a,b,a>0 and b>0))
print('{}> 0 and {} >0 : {}'.format(a,b,a>0 or b>0))
print(False and True)
print(True or True)

print('not {} : {}'.format(a,not a)) # true 반전으로 not
print('not {} : {}'.format(b,not b)) # 0은 false 로 인식