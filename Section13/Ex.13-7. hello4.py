'''
readlines() : 줄단위 용소로 리스트 타입으로 변환
'''


with open('hello.txt','rt',encoding='UTF-8') as file:
    line_list = file.readlines()
    for line in line_list:
        print(line,end='')