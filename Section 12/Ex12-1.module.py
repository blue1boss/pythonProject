'''

모듈(module)
    변수나 함수 또는 클래스를 모아 놓은 파일을 모듈이라고 한다.
    모듈 -> 파일명.py

모듈 사용법
import 모듈명

'''
import converter

miles = converter.kilometer_to_miles(150)
print(f'150km= {miles} miles')

pounds= converter.gram_to_pounds(1000)
print(f'100gram= {pounds} pounds')