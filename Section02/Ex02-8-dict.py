'''
Dictionary
    Key:value 로 이루어져 쌍으로 데이터 값을 저장하는데 사용
'''

thisdict ={
    'brand':'나이키',
    'model': 'Max90',
    'year': 1990
}

# 키 이름을 사용하여 참조할 수 있다.
# 값 가져오기
print(thisdict['brand'])
print(thisdict.get('model'))

#키 목록 가져오기
print(thisdict.keys())

# 추가하기
thisdict = {
    'brand':'Ford',
    'model':'Mustang',
    'year' : 1964
}
thisdict['color']= 'RED'
print(thisdict)
thisdict.update({'bgcolor':'black'})
print(thisdict)

#변경
thisdict['color']= 'Blue'
print(thisdict)
thisdict.update({'bgcolor':'Yellow'})
print(thisdict)

#항목제거하기
thisdict.pop('model')
print(thisdict)

#마지막 삽입된 항목 제거
thisdict.popitem()
print(thisdict)