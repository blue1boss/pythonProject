'''
파일복사
    원본 복사 -> 버퍼(Memory 저장) -> 복사본 쓰기

open() 함수 모드
    b(binary mode) :
        해당 파일의 데이터를 바이너리 파일로 인식하고 입출력
'''

buffer_size = 1024 # 1024바이트 -> 1kb
with open('../Section13/hello.txt','rb')as source: #section 13의 파일을 열자
    with open('hello2.txt','wb') as copy: #파일을 새로 쓰겠다 (없으면)
        while True:
            buffer = source.read(buffer_size) #읽을때 1024만큼 읽겠다,buffer에읽은값 대입
            if not buffer: # 값이 없으면 멈추어라
                break
            copy.write(buffer) #값이 있으니 데이터가 write된것

print('hello2.txt 파일이 복사 되었습니다.')