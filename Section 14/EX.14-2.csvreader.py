'''
csv (comma-separated values)
    필드를 쉼표(,)로 구분한 텍스트 데이터 파일

'''
student_list = [] #리스트 변수 객체 1개 만듬
with open('학생명단.csv','rt',encoding='UTF-8')as file: #열었다 파일
    file.readline() #한줄씩 읽음, 첫줄은 데이터는 없음 넘긴다
    while True:
        line = file.readline()
        if not line:
            break
        student =line.split(',') # 문자열을 , 로 되어있는
        student_list.append(student) # 2중으로 리스트가 들어감
print(student_list)
