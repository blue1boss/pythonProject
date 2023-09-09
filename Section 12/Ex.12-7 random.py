'''
random - 난수 생성 모듈

'''
import random

#두 인자 사이 난수
print(random.randint(1,10)) #1~10사이의 값이 랜덤 출력

print(random.randrange(10)) #0~9사이의 난수 값을 만들어줌
print(random.randrange(1,10))
print(random.randrange(1,10,2)) #1~9중 홀수만 나온다

#0 이상 1미만
print(random.random())

if random.random() < 0.5:
    print('강화에 성공하였습니다!')
else:
    print('강화에 실패하였습니다!')
#choice 함수 - 리스트에서 랜덤
seasons =['spring','summer','fall', 'winter']
print(random.choice(seasons))

#shuffle()함수-임의로 섞는 함수
my_list =[1,2,3,4,5]
random.shuffle(my_list)
print(my_list)