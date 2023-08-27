'''

Set
    고유한 원소로 구성된 변경가능한 컬렉션 타입
    중복값을 허용하지 않는다.
    순서가 없다
'''

thisset ={'피카츄', '라이츄', '파이리'}
print(thisset)
#실행할 때 마다 출력되는 순서가 바뀐다.

#항목 가져오기
for x in thisset:
#thisset의 길이만큼 반복: 1개씩 가져와준다
    print(x)
#값이 있으면 True가 되는 것이다.

#set 의 길이
print(len(thisset))

#값이 있는 확인
thisset = {'피카츄', '잠만보', '메타몽'}
print('피카츄' in thisset)
print('꼬부기' in thisset)

#항목 추가하기
thisset.add('꼬부기')
print(thisset)

#중복값 테스트: 중복값은 허용되지 않는다.
thisset.add('잠만보')
print(thisset)

#다른 Set 항목 추가 : 중복값 시에 1번만 들어감
thisset1 = {'피카츄', '잠만보', '파이리'}
thisset2 = {'꼬부기', '잠만보', '뮤츠'}
thisset1.update(thisset2)
print(thisset1)

# 항목 제거
thisset = {'피카츄', '라이츄', '파이리'}
thisset.remove('피카츄')
print(thisset)

thisset = {'피카츄', '라이츄', '파이리'}
thisset.discard('피카츄')
print(thisset)

#remove() : 없는 항목 삭제시 에러발생
#discard() : 없는 항목 삭제 :에러 발생 안함
thisset.discard ('피카츄')
print(thisset)

#항목 제거 방식 2 : #어떤것을 삭제할지 모름
thisset.pop()
print(thisset)

#비우기
thisset.clear()
print(thisset)
