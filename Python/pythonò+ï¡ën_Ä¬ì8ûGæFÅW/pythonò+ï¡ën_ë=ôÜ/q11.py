#百人一首の一問一答テスト

import random

human_neck = []
index_end = 100
point = 0

with open('q11.py_100human1neck.txt' , mode = 'r' , encoding = 'utf8') as f:
	for s in f:
		human_neck.append(s.replace('\n' , ''))

print('残り:' , len(human_neck) , '問')

for i in range(100):
	
	print('獲得点:' , point)
	index = random.randrange(0 , index_end)

	#print(human_neck[index - 1])#確認用
	#print(human_neck[index])#確認用
	#print(human_neck[index + 1])#確認用
	#print(human_neck[index + 2])#確認用
	
	ans_list = human_neck[index].split('/')
	
	#print('答え:' , ans_list)#答え
	
	print('一の句:',ans_list[0])
	print('二の句:',ans_list[1])
	print('三の句:',ans_list[2])
	
	ans_7_1 = input('四の句:')
	
	ans_7_2 = input('五の句:')
	
	if ans_list[3] == ans_7_1 and ans_list[4] == ans_7_2:
		print('正解')
		point += 1
	elif ans_7_1 == 'あああああ' or ans_7_2 == 'あああああ':
		print('中断')
		break
	else:
		print('不正解')
	human_neck.pop(index)
	index_end -= 1
	print('残り:' , len(human_neck) , '問')
	
	#print(human_neck[index - 1])#確認用
	#print(human_neck[index])#確認用
	#print(human_neck[index + 1])#確認用
	#print(human_neck[index + 2])#確認用

print('最終結果:' , point , '点')
