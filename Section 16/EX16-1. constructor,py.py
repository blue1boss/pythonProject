'''
생성자
    객체를 생성할 때 자동으로 실행(호출)되는 메서드
    주로 객체 초기화 용으로 사용된다.

    생성자 선언방법
    __init()__
'''

class USB:
    def __init__(self,capacity): #실행됨 128로
        self.capacity = capacity

    def info(self):
        print(f'{self.capacity}GB USB')


# 실행코드

usb = USB(128) #capacity 128
usb.info()
#객체에 128 넣어줌

usb2 = USB(1024) #각각 개체 생김
usb.info()