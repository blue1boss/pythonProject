'''
Exception 17-3

a = int(input('제수를 입력하세요 >>>' ))
    b = int(input('피제수를 입력하세요 >>>' ))

    print(f'{a} / {b} = {a/b}')
    이 경우에는 zero error division이 뜨게 된다.
'''

try:
    a = int(input('제수를 입력하세요 >>>' ))
    b = int(input('피제수를 입력하세요 >>>' ))

    print(f'{a} / {b} = {a/b}')
    print('정상종료')

except ValueError:
    print('정수만 입력할 수 있습니다.')
except:
    print('예외가 발생했습니다.')


'''except ZeroDivisionError
    print('0으로 나눌 수 없습니다')'''


#십진수의 값을 넣지 않는 이상은 1.2도 에러가 난다.