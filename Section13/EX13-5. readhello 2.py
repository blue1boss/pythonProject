'''

file 객체 read() 함수
    read() -> 전체 읽어오기
    read(인자값) -> 인자값 크기 만큼 읽어오기

'''
with open('hello.txt','rt',encoding='UTF-8') as file:
    while True:
        str = file.read(5)
        if not str: #읽을 값이 없음 True가 된다.
            break
        print(str)
#개행도 1글자로
