#join()메서드

s = '-'.join('python')
print(s)

s = '+'.join(['a','b','c','d','e'])
print(s)

s = '+'.join(['a','b','c','d','e'])
print(s)


# split() 메서드
s = 'Life is too short'
result = s.split()
print(result)

s= '010-1234-5678'
result = s.split('-')
print(result)
print(result[2])

data = '홍길동|25|프로그래머'
result = data.split('|')
print(f'이름: {result[0]}')
print(f'이름: {result[1]}')
print(f'이름: {result[2]}')

#replace() 메서드 - 문자열 치환
s = 'Life is to short'
result = s.replace('short','long')
print(result)

# strip(), lstrip() , rstrip() 공백제거 메서드
s = '        apple'
result = s.lstrip() #왼쪽 공백제거
print(result)

s = 'apple         '
result = s.rstrip() #오른쪽 공백제거
print(result)

s = '       apple         '
result = s.strip() #양쪽 공백제거
print(result)

s = ' a p p l e '
result = s.strip()
print(result)

s = ' a p p l e '
result = s.replace(' ', '')
print(result)

s = '




