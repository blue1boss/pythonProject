
'''
파일 입출력 (I/O - Input / Output)
    입력(input) 기존파일을 읽어들이는 것
    출력(output) 파일생성, 내용추가를 의미

open()함수
    파이썬에서 open()함수를 사용하여 파일을 열고 파일 객체 생성,
    이를 통해 파일을 읽고 쓸 수 있다 .
'''

'''
file = open('myFile.txt','wt')
print('myFile.txt 파일이 생성되었습니다.')
file.close()
'''
#with 문 : 자동으로 close() 를 해준다.
with open('myFile.txt','wt', encoding ='UTF-8') as file:
    file.write('with 문으로 close 안해요!')
    print('myFile.txt 파일이 생성되었습니다.')