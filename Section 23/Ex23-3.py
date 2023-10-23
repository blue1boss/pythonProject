'''
파일명: Ex23-3-InsertionSort.py

3. 삽입 정렬(Insertion Sort)
    리스트의 모든 요소를 앞에서 부터 차례대로
    이미 정렬된 부분과 비교하여 자신의 위치를 찾아 삽입
'''

'''
arr = [6, 5, 3, 1, 8, 7, 2, 4]
n= 8 (갯수, 길이가 8개이므로) 
i = 1: 
    key = 5
    J= i-1 = 0 
    while 0 >= 0 and 6 > 5 이라 while j >= 0 and arr[j] > key 실행이 되고 
        arr[1] = arr[0] 으로   arr[j + 1] = arr[j]도 실행이 된다 
    j -= 1
    j = -1 
     while -1 >= 0 and 6 > 5 이라 이미 실행이 되지 않음 
     arr[j + 1] = key가 실행
     arr[0] = 5
     
     
     arr = [5, 6, 3, 1, 8, 7, 2, 4]
    i = 2: 
    key = 3
    j = 1
    while 1 >= 0 and arr[1] > 3 이라
    j -= 1
    j = -1 
     while -1 >= 0 and 6 > 5 이라 이미 실행이 되지 않음 
     arr[j + 1] = key가 실행
     arr[0] = 5
     
    '''





def insertion_sort(arr):
    n = len(arr)

    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

    return arr


# 실행코드
arr = [6, 5, 3, 1, 8, 7, 2, 4]
print(insertion_sort(arr))

    '''
    arr = [5, 6, 3, 1, 8, 7, 2, 4]
    n = 8
    i = 1 : 
        key = 5
        j = -1

        while 0 >= 0 and 6 > 5:
           arr[1] = arr[0]
           j -= 1

         arr[0] = 5

    arr = [3, 5, 6, 1, 8, 7, 2, 4]
    i = 2 : 
        key = 3
        j = -1
        조건 j >= 0 and arr[j] > key:
        while -1 >= 0 and arr[0] > 3:
         1번째 반복
            arr[2] = arr[1]
            j -= 1
         2번째 반복
            arr[1] = arr[0]
            j -= 1
        arr[0] = 3

    arr = [1, 3, 5, 6, 8, 7, 2, 4]
    i = 3 :
        key = 1
        j = -1
        조건 j >= 0 and arr[j] > key:
        while 0 >= 0 and 3 > 1:
         1번째 반복
          arr[1] = arr[0]
          j -= 1

         arr[0] = 1

    '''

