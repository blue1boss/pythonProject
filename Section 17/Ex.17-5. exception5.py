'''
exception 5
'''

try:
    raise Exception('강제로 발생시킨 예외')
except Exception as e:
    print('발생한 예외 메세지는 다음과 같습니다')
    print(e)

#except ZeroDivisionError as zde:
#except ValueError as ve:
#print(ve)