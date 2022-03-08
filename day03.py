from pandas import Series, DataFrame
import pandas as pd
import numpy as np

obj = Series([4,7,5,-3])
print(obj)
print(obj.values)
# [ 4  7  5 -3]
print(obj.index)
# RangeIndex(start=0, stop=4, step=1)

'''
series index지정
'''
obj2 = Series([4,7,5,-3], index=['d','b','a','c'])
print(obj2)
print(obj2.index)
# Index(['d', 'b', 'a', 'c'], dtype='object')

print(obj2['a']) # index 색인을 통해 배열 값 접근 가능하다.
# 5 

'''
DF
'''

data = {'state':['Ohio','Ohio','Ohio','Nevada','Nevada'],
        'year':[2000,2001,2002,2002,2005],
        'pop': [1.5,1.5,3.6,1.5,4.0]}

frame = DataFrame(data)
print('data :', data)
print('frame :', frame)
print('data type :', type(data))
print('frame type :', type(frame))