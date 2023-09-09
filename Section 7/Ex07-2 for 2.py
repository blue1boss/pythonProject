pwd=input('비밀번호를 입력하세요>>>')

ch_count = 0
num_count = 0
for ch in pwd:
    if ch.isalpha():
        ch_count += 1
    elif ch.isnumeric():
        num_count += 1

    if ch_count > 0 and num_count > 0:
        print('가능한 비밀번호입니다')
    else:
        print('불가능한 비밀번호입니다')

#input으로 입력값을 받는 것으로 시작함
# ch / num 정수형 변수를 초기화= 변수에다가 처음 대입을 의미
# 변수의 문자열을 하나씩 가지고 와서 그 문자가 isalpha : 문자 True/ 문자아니면 False
# abcd1234 를 넣으면 ch-count 는 4가 되는 것을 의미
# isnumeric 은 숫자값이기에 아래 함수가 실행이 되는 것을 의미 num-count도 4
# 아래 둘다를 맞추면 가능한 비밀번호가 되는 것임 