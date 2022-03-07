import numpy as np

arr = np.arange(10)
#print(arr)

arr2d = np.array([[1,2,3],[4,5,6],[7,8,9]])
#print(arr2d)

'''
색인

개별요소에 접근할때 재귀적으로 접근.
간단하게 콤마로도 접근가능
'''
#print(arr2d[0][2])
# 3
#print(arr2d[0,2])
# 3

arr3d = np.array([[[1,2,3],[4,5,6]], [[7,8,9],[10,11,12]]])

#print(arr3d)
# 다차원 배열에서 마지막색인 생략시 반환되는 객체는 상위 차원의 데이터를 포함하는 ndarray
#print(arr3d[0])

'''
슬라이스 색인
python list 와 동일하게 슬라이싱
'''
#print(arr[1:6])
# [1 2 3 4 5]
#print(arr[:5])
# [0 1 2 3 4]

'''
boolean 색인
'''
names = np.array(['bob', 'joe', 'will', 'bob', 'will', 'joe', 'joe'])
data = np.random.randn(7, 4)

# print("names = ", names)
# names =  ['bob' 'joe' 'will' ' bob' 'will' 'joe' 'joe']

# print("data = ", data)
# data =  [[ 0.6171401  -1.31006154  1.33783327  1.57434132]
#  [ 0.37181771 -0.06528248  0.60074079  0.95944933]
#  [-1.46780531  0.5531589  -0.51698677  1.8942404 ]
#  [ 0.13846992 -1.22735074 -1.74232928  0.4135534 ]
#  [ 1.01430308  0.4947191   0.35755472  1.16755705]
#  [-1.10735558 -0.03861831  0.58564727  0.35433163]
#  [ 0.49550842  1.18493852  0.04833994 -1.47787511]]

# print(names == 'bob')
# [ True False False  True False False False]

print(data[names == 'bob'])
# [[ 0.72199008  0.79560273  0.37148765  0.66597505]
#  [ 0.20000754 -1.20287517 -0.92340088  0.69658497]]

print(data[names == 'bob',2:])
# [[ 0.37148765  0.66597505]
#  [-0.92340088  0.69658497]]

arr_f = np.empty((8,4))

for i in range(8):
    arr_f[i] = i

print(arr_f)
# [[0. 0. 0. 0.]
#  [1. 1. 1. 1.]
#  [2. 2. 2. 2.]
#  [3. 3. 3. 3.]
#  [4. 4. 4. 4.]
#  [5. 5. 5. 5.]
#  [6. 6. 6. 6.]
#  [7. 7. 7. 7.]]

'''
특정로우 선택
'''
print(arr_f[[4,3,0,6]])
print(arr_f[[-3,-5,-7]]) # 음수 : 끝에서부터 역순으로 선택
print('---------------')

arr_i = np.arange(32).reshape((8,4))
'''
ix_()사용 시 1차원 정수배열 2개를 사격형 영역에서 사용할 색인으로 변환해준다.
'''
print(arr_i[np.ix_([1,5,7,2], [0,3,1,2])])

arr = np.arange(15).reshape((3,5))
print(arr)
# [[ 0  1  2  3  4]
#  [ 5  6  7  8  9]
#  [10 11 12 13 14]]
''' 전치 '''
print(arr.T)
# [[ 0  5 10]
#  [ 1  6 11]
#  [ 2  7 12]
#  [ 3  8 13]
#  [ 4  9 14]]

''' 유니버셜 함수 '''

arr = np.arange(10)
print(np.sqrt(arr))
print(np.exp(arr))

#np.save("test", arr)

'''
dot()
'''

a = np.array([1,2,3])
b = np.array([3,4,5])

print("np.dot(a,b) :",np.dot(a,b))