import numpy as np

arr = np.array([1,2,3,4,5])
print(arr)
print(arr.sum())
print(arr.mean())
arr1 = np.array([[1,2,3],[4,5,6]]) # 2차원 배열
arr2 = np.array([[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]]) # 3차원 배열
print(arr2)
print(arr2[:][0])
print("")
print(arr1[:][1])
print("")
print(arr2[0][0][1])

list1 = [[1,2,3],[4,5,6]]
print(list1)

np.arr = np.array(list1) # numpy 2차원 배열 선언
print(np.arr)
print(np.arr[:,2])

arr3 = np.array([[1,2],[3,4]])
print(arr3.transpose()) # 전치행렬로 변환

arr4 = np.array([1,2,3])
arr5 = np.array([4,5,6])

arr_sum = arr4 + arr5 # 배열의 + 연산 ->[5 7 9]
print(arr_sum)

list1 = ([1,2,3])
list2 = ([4,5,6])
list_sum = list1 + list2 # 리스트의 + 연산 ->[1,2,3,4,5,6]
print(list_sum)

arr_multi = arr4 * arr5 # 배열의 * 연산
print(arr_multi)

print(arr4 + 1) # arr4의 원소마다 1이 더해짐
# print(list + 1) # error 발생

print("-----------------------------------")
arr6 = np.array([[1,2,3],[4,5,6],[7,8,9]])
arr7 = np.array([[2,8,4],[1,2,9],[5,1,2]])

arr_index_sum = arr6[:,0] + arr7[:,2]
print(arr_index_sum)

list3 = [1,2,3,4,5,6,7,8,9]
arr8 = np.array(list3)

arr9 = arr8 > 5
print(arr9)

ary10 = np.random.random(5) # 0~1 사이에서 5개의 랜덤수 출력
print(ary10)
print(np.all(ary10 >= 3)) # 모든 원소가 0.3 이상이면 True (and 조건)
print(np.any(ary10 >= 0.3)) # 원소중 1개이상 0.3 이상이면 True (or 조건)

print("-----------------------------------")
print(np.linspace(0,18,6))

month = 1
while month <= 12:
    print(f'2020년 {month}월')
    month = month + 1
