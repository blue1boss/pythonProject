import random
import time

#[1,2,3,4,5,.....,45]
# 하나씩 n에 숫자가 들어감
pot = [n for n in range(1,46)]

jackpot=[]

for n in range(1,7) : #1-6까지 반복
    random.shuffle(pot) #리스트 순서 섞는다

    pick = pot.pop()
    print(f'{n}번째 당첨번호는 {pick}입니다')
    jackpot.append(pick)
    time.sleep(1) #1초동안 프로그램 일시정지

jackpot.sort()
print(f'이번당첨번호는 {jackpot}입니다')
