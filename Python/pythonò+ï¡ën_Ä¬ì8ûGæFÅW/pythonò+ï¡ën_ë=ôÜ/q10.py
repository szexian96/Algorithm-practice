#じゃんけんゲームのプログラム(香川県TODあり)

import random
import time

dic = {"a": "グー", "b": "チョキ", "c": "パー"}

for i in range(1):
	print("じゃーんけーん")

	time_sta = time.perf_counter()#計測開始

	print("a=グー　b=チョキ　c=パー　aかbかcを入力")
	user = input('>>>  ')
	
	time_end = time.perf_counter()#計測終了
	time_judg = time_end - time_sta#経過時間測定
	kagawa_tod = random.randint(1,47)#対戦相手が住む県を特定
	#kagawa_tod = 47#対戦相手が香川県民確定
	if (time_judg > 3600.0) and (kagawa_tod == 47):#香川県TOD判定
		print('対戦相手が香川県民で対戦時間が1時間を超えたのであなたの勝利')
		break
	
	user = user.lower()

	try:
		user_choice = dic[user]

		choice_list = ["a", "b", "c"]
		pc = dic[random.choice(choice_list)]

		draw = 'DRAW'
		win = 'You Win!!'
		lose = 'You lose!!'

		if user_choice == pc:
			judge = draw
		else:
			if user_choice == "グー":
				if pc == "チョキ":
					judge = win
				else:
					judge = lose

			elif user_choice == "チョキ":
				if pc == "パー":
					judge = win
				else:
					judge = lose

			else:
				if pc == "グー":
					judge = win
				else:
					judge = lose

		print("あなた選んだのは %s" % user_choice)
		print("対戦相手が選んだのは %s" % pc)
		print("結果は%s" % judge)
	except:
		print("aかbかcを入力してください。")
