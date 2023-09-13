'''
함수의 종료를 위한 return
'''

def charge(energy):
    if energy < 0:
        print('0보다 작은 에너지는 충전할 수 없습니다.')
    else:
        print('에너지가 충전되었습니다.')

charge(1)
charge(-1)