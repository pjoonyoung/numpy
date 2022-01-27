import numpy as np

arr1 = np.random.rand(5) # 0~1 사이에서 5개의 랜덤수(난수) 어레이 생성
print(arr1)
print("")
arr2 =np.random.rand(2,3) # 2행 3열의 난수 어레이를 생성
print(arr2)

print("------------------------------------")
# randint 함수
arr3 = np.random.randint(3,size=5) # 0 <= n < 3(n은정수) 인 난수 5개 출력
print(arr3)