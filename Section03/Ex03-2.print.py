'''
print() 함수 사용법
    sep: 출력할 value의 구분 문제
    end: value 출력 후 출력할 문자(기본값 '\n')
    file: 출력 방향 지정
'''

print('재미있는', '파이썬')
print('Pyton','Java','C',sep=',')
print('Pyton','Java','C',sep='0')
#맨뒤 옵션을 주지 않으면, 띄어쓰기로 연결

print('안녕', end='\n')
print('하세요')

print('안녕', end='')
print('하세요')

fos= open('sample.py', mode='wt') #mode=wt
print('print("Hello,World")',file =fos)
fos.close()
#파일을 만들고, 파일 읽어오기가 가능하다
fos= open('sample.py', mode='wt')
print('print("Hello,World")',file =fos)
fos.close()