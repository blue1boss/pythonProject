'''
continue
    while 문이나 for 문과 같은 반복문을 강제로 건너뛰게 한다.
'''

total = 0
for a in range(1 ,101): #1~100까지 연속된수
    if a % 3 == 0: #3으로 나눈 나머지가 0이라는 것 3의배수를 의미
            continue
    total += a
    print(f'a:{a}, total {total}') #토탈은 누적의 숫자를 의미

print(total)