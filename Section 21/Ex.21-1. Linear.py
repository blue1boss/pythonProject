'''
21. Linear
자료 구조
    데이터를 구조화하고 저장하는 방법을 나타낸다
    효율적인 데이터 조작을 지원하는 구조체 /클래스

알고리즘
    주어진 문제를 해결하기 위한 계산 과정 절차를 나타낸다


선형리스트 (Linear list)
    간단한 자료구조 중 하나로, 데이터를 일렬로 나열한 구조체

'''


class LinearList():

    def __init__(self):
        self.linear = [] #빈 리스트 생성

    #리스트에 데이터 추가
    def add_data(self,data):
        linear = self.linear
        linear.append(None)
        lLen= len(linear)
        linear[lLen - 1] = data


#데이터 삽입
    def insert_data(self, position, data):
        linear= self.linear

        if position < 0 or position > len(linear):
            print('데이터 범위 벗어')
            return

        linear.append(None) #none 값 하나 추가하는 것
        linearSize=len(linear)

        for i in range(linearSize - 1, position, -1): #for 로 땡겨주는 것  5, 4 none이 5번 자리이고 값을 4에 넣어라
            linear[i]= linear[i-1]
            linear[i-1]= None

        linear[position]= data


#아래 추가 삭제 위해서 쓰는 코드
    '''
    def delete_date(self,position):
        linear = self.linear

        if position < 0 or position > len(linear) :
            print('범위 벗어남')
            return

        linear[position]= None
        linearSize = len(linear)

        for i in range(position + 1, linearSize):
            linear[i-1] = linear[1]
            linear[i] = None

        del(linear[linearSize -1])

'''

#실행코드

linear = LinearList()
linear.add_data(3)
linear.add_data(5)
linear.add_data(4)
linear.add_data(2)
linear.add_data(6)

linear.insert_data(3,99)

#linear.delete_data(2)#추가

print(linear.linear)


