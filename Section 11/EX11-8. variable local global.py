#전역변수 선언
total = 0

def gift(dic, who, money):
    global total
    total += money
    dic[who] =money

#https://pythontutor.com/render/html#mode=display
wedding = {}
name = '영희'
gift(wedding, name, 5)
print(total)
gift(wedding,'철수', 6)
gift(wedding, '이모', 10)
print(f'축의금 명단: {wedding}') #wedding이라는 dic 에 추가를 시키는 것
print(f'전체 축의금: {total}') # 전체 money 더하는 것이므로 21이 나오게 되는 것

#gift 함수 (참조, 값, 값) 함수가 시작이 되면서 dic[who]money함수 실행이 된다
#dic의 who에는 money 가 들어가게 됨