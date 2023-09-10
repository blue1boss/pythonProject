'''

이름/국어/영어/수학
John / 90/ 85 / 95
Emily / 92/ 88/ 96
Michael /98/ 90/ 92
Jessica/ 88/ 82/ 78

문제
    위 데이터 하나의 변수로 만들어보세요.

    그 변수 위와 같이 출력해보세요.
'''


students = [
    {'이름': 'John', '국어': '90', '영어': '85', '수학' : '95'},
    {'이름': 'Emily', '국어': '92', '영어': '88', '수학' : '96'},
    {'이름': 'Michael', '국어': '98', '영어': '90', '수학' : '92'},
    {'이름': 'Jessica', '국어': '88', '영어': '82', '수학' : '78'}
]

#테이블 헤더 출력
print('이름/국어/영어/수학')

#각 학생의 성적 출력
for student in students:
    name = student['이름']
    kor = student['국어']
    eng= student['영어']
    math = student['수학']
    print(f'{name}/{kor}/{eng}/{math}')

print(type(students[0]))
print(students[1])
print(students[1]['영어'])
#list 1번의 index에서 emily 들어간 부분, 영어의 key값을 가져와서 -> value값 88을 가지고 옴

std_dict = studnets[1]
print(students[1]['영어'])

'''
dict 1= {'이름': 'John', '국어': '90', '영어': '85', '수학' : '95'}
dict 2= {'이름': 'Emily', '국어': '92', '영어': '88', '수학' : '96'}
dict 3= {'이름': 'Michael', '국어': '98', '영어': '90', '수학' : '92'}
'''

