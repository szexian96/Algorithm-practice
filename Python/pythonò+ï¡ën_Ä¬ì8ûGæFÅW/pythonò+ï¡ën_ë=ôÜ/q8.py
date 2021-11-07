import re

data = {'2021/1/1 00:00:00':{'菅直人':1,'菅田将暉':10,'浜菅':22},'2021/1/2 12:12:12':{'菅首相':2,'麻生':4,'菅さん':8},'2021/1/3 13:00:00':{'菅首相':3}}

"""
data{
	'2021/1/1 00:00:00':{
		'菅直人':1
	},
	'2021/1/2 12:12:12':{
		'菅首相':2,'麻生':4,'菅さん':8
	},
	'2021/1/3 13:00:00':{
		'菅首相':3
	}
}
"""
print(data,'\n')

kensaku = input('検索キーワード:')#バリューのキーのキーワード検索をする

seikirenketu = '.*' + kensaku +'.*'

datavalues = list(data.values())
#print(datavalues)

datalist = []
dataonlylist = []

for i in range(len(datavalues)):
	dk=list(datavalues[i].keys())
	datalist.extend(dk)
	#print(datalist)
dataset = list(set(datalist))#重複を除外
#print(dataset)

for i in range(len(dataset)):
	m = re.search(seikirenketu, dataset[i])
	if m != None:
		#print(m.group())
		dataonlylist.append(m.group())#extendだと分割挿入

print('検索結果:')
print(dataonlylist)
