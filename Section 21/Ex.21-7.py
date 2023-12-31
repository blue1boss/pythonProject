'''
힙(Heap)
    최대값 및 최소값 찾아내는 연산을 빠르게 하기 위해 고안된 완전 이진트를 기본으로 한 자료구조

'''

import heapq

class MinHeap:

    def __init__(self):
        self.heap = []

    def push(self,val):
        heapq.heappush(self.heap, val)

    def pop(self):
        return heapq.heappop(self.heap)

#실행코드
heap = MinHeap()
heap.push(3)
heap.push(1)
heap.push(4)
heap.push(2)
heap.push(5)

print('-----MinHeap-----')
print(heap.pop())
print(heap.pop())
print(heap.pop())
print(heap.pop())
print(heap.pop())

#숫자를 서로 비교하여 더 큰걸 위로 올리고 내리고 가는 형태

class MaxHeap:
    def __init__(self):
        self.heap = []

    def push(self, val):

        heapq.heappush(self.heap, -val)

    def pop(self):
        return -heapq.heappop(self.heap)

# 실행코드
heap = MaxHeap()
heap.push(3)
heap.push(1)
heap.push(4)
heap.push(2)
heap.push(5)

print('----- MaxHeap -----')
print(heap.pop())
print(heap.pop())
print(heap.pop())
print(heap.pop())
print(heap.pop())