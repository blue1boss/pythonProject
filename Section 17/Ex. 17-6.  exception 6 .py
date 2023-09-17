'''
17-6
'''
import traceback
try:
    score= int(input('점수를 입력하세요.'))
    if score < 0 or score > 100:
        raise Exception('점수는 0에서 100 사이입니다')
except Exception as e:
    print(e)
    traceback.print_exc()
else:
    if score > 60:
        print(f'{Score}점은 합격입니다')
    else:
        print(f'{Score}점은 불합격입니다')
