#対応するデータを入力すると相関係数を表示するプログラム
"""
実行例の入力物:
15
76
73
71
64
71
66
71
73
66
66
69
72
75
70
70
153
141
144
129
147
138
142
143
135
131
139
147
148
139
140
"""

import math

datalist_x = []
datalist_y = []
squlist_x = []
squlist_y = []
multlist_xy = []


num = int(input('データ数:'))

def datainput():
	for x in range(num):
		x = x + 1
		print('x%d:' %x , end = '')
		x = x - 1
		data_x = int(input())
		datalist_x.append(data_x)
	
	for y in range(num):
		y = y + 1
		print('y%d:' %y , end = '')
		y = y - 1
		data_y = int(input())
		datalist_y.append(data_y)

def datasquare():
	for x in range(num):
		squlist_x.append(datalist_x[x]**2)
	
	for y in range(num):
		squlist_y.append(datalist_y[y]**2)

def multiplication():
	for i in range(num):
		multlist_xy.append(datalist_x[i] * datalist_y[i])


datainput()

datasquare()

multiplication()

sum_x = sum(datalist_x)
sum_y = sum(datalist_y)
squsum_x = sum(squlist_x)
squsum_y = sum(squlist_y)
multsum_xy = sum(multlist_xy)

devsum_x = squsum_x - (sum_x**2) / num
devsum_y = squsum_y - (sum_y**2) / num
devsum_xy = multsum_xy - (sum_x * sum_y) / num
multdevsum_xy = devsum_x * devsum_y
"""
rdevsum_x = round(devsum_x , 3)
rdevsum_y = round(devsum_y , 3)
rdevsum_xy = round(devsum_xy , 3)
rmultdevsum_xy = rdevsum_x * rdevsum_y
"""
correlation_coefficient = devsum_xy / math.sqrt(multdevsum_xy)

#rcorrelation_coefficient = rdevsum_xy / math.sqrt(rmultdevsum_xy)
"""
print('xデータ')
print(datalist_x , '\n')
print('yデータ')
print(datalist_y)
print('x^2データ')
print(squlist_x , '\n')
print('y^2データ')
print(squlist_y , '\n')
print('x*yデータ')
print(multlist_xy , '\n')

print('x合計:' , sum_x , '\n')
print('y合計:' , sum_y , '\n')
print('x二乗和: ' ,squsum_x , '\n')
print('y二乗和:' , squsum_y , '\n')
print('xy積和:' , multsum_xy , '\n')

print('x偏差平方和:' , devsum_x , '\n')
print('y偏差平方和:' , devsum_y , '\n')
print('xy偏差積和:' , devsum_xy , '\n')

print('x偏差平方和(.以下3桁四捨五入):' , rdevsum_x , '\n')
print('y偏差平方和(.以下3桁四捨五入):' , rdevsum_y , '\n')
print('xy偏差積和(.以下3桁四捨五入):' , rdevsum_xy , '\n')
"""
print('相関係数:' , correlation_coefficient , '\n')
"""
print('相関係数(.以下3桁四捨五入):' , round(correlation_coefficient , 3) , '\n')

print('相関係数(.以下3桁四捨五入したもので計算し.以下3桁四捨五入):' , rcorrelation_coefficient , '\n')
"""
