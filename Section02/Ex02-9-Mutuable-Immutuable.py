'''

mutable - 메모리에서 값을 변경 가능 객체
    리스트(list), 세트(set), 딕셔너리(dict)...등
'''

me = [1,2,3]
print(me)
print(id(me))
#id는 수정이후에도 같다 : 주소값이 변경되지 않음
me.append(4)
print(me)
print(id(me))

'''
immutable- 메모리 값 변경 불가 
    정수(int), 실수(float), 문자열(str), 튜플(tuple)  
'''
imme = 10
print(imme)
print(id(imme))

imme += 1 #imme = imme +1 을 하겠다는 것과 같다
print(imme)
print(id(imme))
#새로 주소가 만들어진다

imme2 = 10
print(imme2)
print(id(imme2))

print('========')
#id값 확인하기 튜플
thistuple = ('피카츄', '라이츄', '파이리')
print(thistuple)
print(id(thistuple))
#casting(형변환) ['피카츄', '라이츄', '파이리']
thiscast= list(thistuple)
thiscast[1]='잠만보'
thistuple =tuple(thiscast)
#('피카츄', '라이츄', '파이리')
print(thistuple)
print(id(thistuple))



