import collections
import math

#データ
data = [112,122,125,119,121,118,113,120,119,113]
print('データ',data)

#合計値
sum = sum(data)
print('合計値',sum)

#平均値
ave = sum / len(data)
print('平均値',ave)

#中央値
data.sort()
print('昇順ソート',data)
data_med = []
if len(data) % 2 == 0:
	data_med.append(data[int(len(data) / 2 - 1)])
	data_med.append(data[int(len(data) / 2)])
	#print('偶数中央配列',data_med)
	data_med_sum = data_med[0] + data_med[1]
	med = data_med_sum / len(data_med)
else:
	med = data[int((len(data) - 1) / 2)]
print('中央値',med)

#最頻値
data_counter = dict(sorted(dict(collections.Counter(data)).items(), key=lambda x:x[1], reverse=True))
#print('カウント',data_counter)

value_max = max(data_counter.values())
#print('最頻値出現回数',value_max)
for mode,count in data_counter.items():
	if value_max == count:
		print('最頻値',mode)
	else:
		break

#範囲
min = data[0]
max = data[len(data) - 1]
range = max - min
print('範囲',range)

#第1四分位数
data_low = []
data_low_med = []

if len(data) % 2 == 0:
	low_add1 = int(len(data) / 2 - 1) + 1
	data_low.extend(data[0:low_add1])
	#print('偶数第1四分位配列',data_low)
else:
	low_add2 = int((len(data) - 1) / 2)
	data_low.extend(data[0:low_add2])
	#print('奇数第1四分位配列',data_low)

if len(data_low) % 2 == 0:
	data_low_med.append(data_low[int(len(data_low) / 2 - 1)])
	data_low_med.append(data_low[int(len(data_low) / 2)])
	#print('偶数第1四分位中央配列',data_low_med)
	data_low_sum = data_low_med[0] + data_low_med[1]
	low_med = data_low_sum / len(data_low_med)
else:
	low_med = data_low[int((len(data_low) - 1) / 2)]
print('第1四分位数',low_med)

#第3四分位数
data_top = []
data_top_med = []

if len(data) % 2 == 0:
	top_add1 = int(len(data) / 2 - 1) + 1
	data_top.extend(data[top_add1:len(data)])
	#print('偶数第3四分位配列',data_top)
else:
	top_add2 = int((len(data) - 1) / 2) + 1
	data_top.extend(data[top_add2:len(data)])
	#print('奇数第3四分位配列',data_top)

if len(data_top) % 2 == 0:
	data_top_med.append(data_top[int(len(data_top) / 2 - 1)])
	data_top_med.append(data_top[int(len(data_top) / 2)])
	#print('偶数第3四分位中央配列',data_top_med)
	data_top_sum = data_top_med[0] + data_top_med[1]
	top_med = data_top_sum / len(data_top_med)
else:
	top_med = data_top[int((len(data_top) - 1) / 2)]
print('第3四分位数',top_med)

#四分位範囲
qua_range = top_med - low_med
print('四分位範囲',qua_range)

#四分位偏差
qua_dev = qua_range / 2
print('四分位偏差',qua_dev)

#偏差平方和
squ_sum = 0
for i in data:
	squ_sum+= i**2
#print('二乗和',squ_sum)

dev_sum = squ_sum - (sum**2) / len(data)
print('偏差平方和',dev_sum)

#分散
dis = dev_sum / (len(data) - 1)
print('分散',dis)

#標準偏差
stan_dev = math.sqrt(dis)
print('標準偏差',stan_dev)
