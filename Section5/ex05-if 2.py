age=int(input('나이를 입력하세요:'))

if age < 5:
    print('어린이들을 위한 놀이공원을 추천합니다')
elif age >= 5 and age < 18:
    print('당신은 학생이군요')
elif age > = 18 and age < 40:
    print('인생은 여행인 성인이군요')
elif age > = 40 and age < 60:
    print('여가시간이 필요하네요')
else:
    print('평화로운 생활이 필요한 시점입니다')

