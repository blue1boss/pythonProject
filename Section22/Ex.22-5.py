'''
파일명: Ex22-5-O(n^2).py

O(N^2)
    제곱 시간 복잡도, 중첩 반복문을 사용하는 알고리즘
'''

# 선택 정렬 알고리즘 : 가장 작은 숫자를 찾아서 자리를 찾아주는 정렬이다.

'''idx 0  1  2  3  4
arr = [1, 3, 4, 5, 2]
i : 0 
   min_idx = 3
   조건: arr[j] < arr[min_idx] 
   j: 1  -> arr[1] < arr[0] : true => min_idx = 1
   j: 2  -> arr[2] < arr[1] : false 
   j: 3  -> arr[3] < arr[1] : true => min_idx = 3
   j: 4  -> arr[4] < arr[3] : false 

   // 변수 값 스왑
   arr[0], arr[3] = arr[3], arr[0]

   idx 0  1  2  3  4
arr = [1, 2, 4, 5, 3]

i : 1
   min_idx = 4
   조건: arr[j] < arr[min_idx] 
   j: 2  -> arr[2] < arr[1] : false
   j: 3  -> arr[3] < arr[1] : false
   j: 4  -> arr[4] < arr[1] : true  => min_idx = 4


   arr[1], arr[4] = arr[4], arr[1]

   idx 0  1  2  3  4
arr = [1, 2, 3, 5, 4]
i : 2
    min_idx = 4
    j: 3 -> arr[3] < arr[2] : false
    j: 4 -> arr[4] < arr[2] : true   => min_idx = 4

     arr[2], arr[4] = arr[4], arr[2]

   idx 0  1  2  3  4
arr = [1, 2, 3, 4, 5]
i : 3
    min_idx = 3
    j: 4 -> arr[4] < arr[3] : true   ==> min_idx = 4

    arr[3], arr[4] = arr[4], arr[3]

   idx 0  1  2  3  4
arr = [1, 2, 3, 4, 5]

i : 4
    min_idx = 4
    arr[4], arr[4] = arr[4], arr[4]

   // j: 3  -> arr[3] < arr[2] : ? => min_idx = ?


'''

'''
arr= [5,3,4,1,2] 
5번 실행될 예정 
i가 0이면 
    min_idx= 0 
    for j in range(i+1, len(arr)): 1부터 5까지 인데, j는 1,2,3,4까지 들어감 
    j: 1 
        arr[1]< arr[0]: 3< 5 가 ture 면 min_idx에 j를 넣게 된다 
        min_idx = 1 
        for 문 실행이 되서 
        j: 2일때 -> arr[2]< arr[1] 은 4<3 은 false 가 된다 
        J: 3이면 arr[3] < arr[1] 으로 true min_inx=3
        J: 4 -> arr[3]< arr[3] : false - min_idx= 3
        //변수 값 스왑 arr[i] , arr[min_ind]
        arr[0]. arr[3] = arr[3], arr[0]
        
        i는 1이면 
        min_idx = 1
        arr[j] < arr[min_idx] 
        j: 2  -> arr[2] < arr[1] : false
        j: 3  -> arr[3] < arr[1] : false
        j: 4  -> arr[4] < arr[1] : true  => min_idx = 4

         //변수 값 스왑 arr[i] , arr[min_ind]
        arr[1], arr[4] = arr[4], arr[1]
        
        idx 0  1  2  3  4
        arr = [1, 2, 4, 5, 3] 이 된다 
        
        i : 2
        min_idx = 2 
        j: 3 -> arr[3] < arr[2] : false
        j: 4 -> arr[4] < arr[2] : true   => min_idx = 4

        arr[2], arr[4] = arr[4], arr[2]
        idx 0  1  2  3  4
        arr = [1, 2, 3, 5, 4] 이 된다 
        
        i : 3
        min_idx = 3
        j: 4 -> arr[4] < arr[3] 4< 5 : true   ==> min_idx = 4
        arr[3], arr[4] = arr[4], arr[3]
        arr = [1, 2, 3, 4, 5] 이 된다 
        
        i : 4
        min_idx = 4, j가 5가 되어 실행하지 않는다 교체시에 같은 값을 대입하는 것에 불과하다. 
        arr[4], arr[4] = arr[4], arr[4]
        // j: 3  -> arr[3] < arr[2] : ? => min_idx = ?
'''
def selection_sort(arr):
    for i in range(len(arr)):

        min_idx = i

        for j in range(i + 1, len(arr)):

            if arr[j] < arr[min_idx]:
                min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr


# 실행코드
arr = [5, 3, 4, 1, 2]
print(selection_sort(arr))