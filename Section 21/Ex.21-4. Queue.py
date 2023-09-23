'''
21-4. Queue.py

큐(Queue)
    기본적으로 자료구조 한가지로, 먼저 넣은 데이터가 먼저 나오는
    FIFO(First in First out)
'''

def Queue():
    queue = []
    queue.append(1)
    queue.append(2)
    queue.append(3)
    queue.append(4)
    queue.append(5)
    while queue:
        print(f'Get Value: {queue.pop(0)}') #0번째 인덱스 가져오겠다

#실행코드
Queue()


