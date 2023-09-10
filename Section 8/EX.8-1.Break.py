
'''
break 문
    while문이나 for문과 같은 반복문을 강제로 종료하는 명령어
'''
n=1
while True:
    print(n)
    n += 1

n=1
while True:
    print(n)
    if n == 10: #10과 같은지 비교, 1씩 증가시키는 형태
        break
    n += 1