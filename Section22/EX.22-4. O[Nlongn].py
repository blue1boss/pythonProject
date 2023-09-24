'''
22-4

O(NlogN)
    선형 로그 시간 복잡도, 병합 정렬 등의 알고리즘

머지정렬: 낮은 것 부터 오는 형태


arr = [5, 2, 8, 6, 1, 9, 3, 7]
mid =4 (8/2)
merge_sort(arr[:4]) 앞에서부서 4개  print(arr[:4])
merge_sort([5,2,8,6])

    mid = 2
    merge_sort(arr[:2])
    merge_sort([5,2])
        mid = 1
        merge_sort([5])
        길이가 1개 이하라 결과가 바로 return이 되는 것

    merge_sort([2]) -> [2]


    merge(
'''



def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left, right):
    result = []

'''
merge([5],[2]) 
result =[]
while i < len(left) and j < len(right): 둘다 1이다 
if left[i] < right[j]: 5<2 는 거짓으로 실행되지 않음 

result = []
i = 0 
j = 1
0 < 1 1<1 로 오른쪽 항목이 거짓이 되어 I 문이 끝나게 된다 

result += left[i: ] 
result += right[J: ] 

merge([5],[2]) = [2,5]
'''


    i = j = 0
    while i < len(left) and j < len(right):

        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result += left[i:]
    result += right[j:]

    return result


arr = [5, 2, 8, 6, 1, 9, 3, 7]
sorted_arr = merge_sort(arr)
print(sorted_arr)