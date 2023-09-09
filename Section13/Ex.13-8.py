'''

'''

with open('hello.txt','rt',encoding='UTF-8') as file:
    line_list = file.readlines()
    for no, line in enumerate(line_list):
        print(f'{no+1} {line}',end='')