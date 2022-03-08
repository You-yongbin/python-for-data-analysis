from pandas import NA, Series, DataFrame
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

obj = Series([4.5,7.2,-5.3,3.6], index=['d','b','a','c'])
obj2 = obj.reindex(['a','b','c','d','e'])

print(obj)
# d    4.5
# b    7.2
# a   -5.3
# c    3.6
# dtype: float64
print(obj2)
# a   -5.3
# b    7.2
# c    3.6
# d    4.5
# e    NaN
# dtype: float64

'''
df ix 색인
'''
data = pd.DataFrame(np.arange(16).reshape((4, 4)),
                    index=['Ohio', 'Colorado', 'Utah', 'New York'],
                    columns=['one', 'two', 'three', 'four'])
print(data)
#           one  two  three  four
# Ohio        0    1      2     3
# Colorado    4    5      6     7
# Utah        8    9     10    11
# New York   12   13     14    15

#print( data.ix['Colorado', ['two','three']] )
print( data.loc['Colorado', ['two','three']] )
# two      5
# three    6
print( data.loc[['Colorado','Utah'], ['two','three','one']] )
#           two  three  one
# Colorado    5      6    4
# Utah        9     10    8

s1 = pd.Series([7.3, -2.5, 3.4, 1.5], index=['a', 'c', 'd', 'e'])
s2 = pd.Series([-2.1, 3.6, -1.5, 4, 3.1], index=['a', 'c', 'e', 'f', 'g'])
print(s1+s2)

df1 = pd.DataFrame(np.arange(9.).reshape((3, 3)), columns=list('bcd'), index=['Ohio', 'Texas', 'Colorado'])
df2 = pd.DataFrame(np.arange(12.).reshape((4, 3)), columns=list('bde'), index=['Utah', 'Ohio', 'Texas', 'Oregon'])

print(df1)
#             b    c    d
# Ohio      0.0  1.0  2.0
# Texas     3.0  4.0  5.0
# Colorado  6.0  7.0  8.0
print(df2)
#           b     d     e
# Utah    0.0   1.0   2.0
# Ohio    3.0   4.0   5.0
# Texas   6.0   7.0   8.0
# Oregon  9.0  10.0  11.0
print(df1+df2)
#             b   c     d   e
# Colorado  NaN NaN   NaN NaN
# Ohio      3.0 NaN   6.0 NaN
# Oregon    NaN NaN   NaN NaN
# Texas     9.0 NaN  12.0 NaN
# Utah      NaN NaN   NaN NaN

df1 = DataFrame(np.arange(12).reshape((3,4)), columns=list('abcd') )
df2 = DataFrame(np.arange(20).reshape((4,5)), columns=list('abcde') )
print(df1+df2)
#       a     b     c     d   e
# 0   0.0   2.0   4.0   6.0 NaN
# 1   9.0  11.0  13.0  15.0 NaN
# 2  18.0  20.0  22.0  24.0 NaN
# 3   NaN   NaN   NaN   NaN NaN
print(df1.add(df2, fill_value=0))
# add, sub, div, mul

s2 = Series(range(3), index=['b','e','f'])
print(s2)

'''
rank
'''
obj = Series([7,-5,7,4,2,0,4])

print(obj)
print(obj.rank())

# from pandas_datareader import data
# all_data = {}
# for ticker in ['AAPL', 'IBM', 'MSFT', 'GOOG']:
#         all_data[ticker] = data.DataReader(ticker, 'google', '2015-01-01', '2016-01-01')

# price = pd.DataFrame({tic : data['Close'] for tic, data in all_data.items()})
# volume = pd.DataFrame({tic : data['Volume'] for tic, data in all_data.items()})

string_data = Series(['aardvark','artichoke',np.nan, 'avocado'])
print(string_data)
# 0     aardvark
# 1    artichoke
# 2          NaN
# 3      avocado
# dtype: object
print(string_data.isnull()) # NaN 값만 True로 검출
# 0    False
# 1    False
# 2     True
# 3    False
# dtype: bool
print(string_data.notnull()) # NaN 이 아닌 실제 값만 True로 검출
# 0     True
# 1     True
# 2    False
# 3     True
# dtype: bool
print(string_data.dropna())

df = DataFrame(np.random.randn(7,3))
df.loc[:4, 1] = NA
df.loc[:2, 2] = NA
print(df)
print(df.dropna())
print(df.dropna(thresh=3))