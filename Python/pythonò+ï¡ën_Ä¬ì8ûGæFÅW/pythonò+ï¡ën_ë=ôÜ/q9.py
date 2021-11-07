#条件分岐訓練
"""わかっていること
・×印はマスである。
・暗い色の部分は上層部で明るい部分は下層部であり、直線の長さは表記の10倍である。
・スタート地点は(A)である。
・(E)と(H)は中継地点であり、(E)→(H)の順序である。
・各マスに辿り着いたときそこは、「アタリ」、「アタリが近い」、「ハズレ」のどれかであり、各確率は等しい。
・「アタリ」のとき、スタート地点から「アタリ」になるまで辿ったルートを表示する。
・「アタリが近い」のとき、画像の直線で結ばれている先のマスは「アタリ」か「アタリが近い」であり、直線の長さが短いマスが次に辿るマスとなる。
・「ハズレ」のとき、次の中継地点へ飛ぶこととする。((A)のときは(E)、(E)のときは(H)へ飛ぶ)
・中継地点(H)に辿り着いたとき、そこは「アタリ」か「アタリが近い」であるため、最後に辿り着く「アタリ」は(I)である。
"""

import random

a = random.randint(0,2)
b = 3
c = 3
d = 3
e = 3
f = 3
g = 3
h = 3
i = 3


for i in range(1):

	if a == 0:
		e = random.randint(0,2)
		print('a')
	elif a == 1:
		b = random.randint(1,2)
		print('a')
	elif a == 2:
		print('atari:a')
		break

	if b == 1:
		d = random.randint(1,2)
		print('b')
	elif b == 2:
		print('atari:a-b')
		break

	if d == 1:
		c = 2
		print('d')
	elif d == 2:
		print('atari:a-b-d')
		break

	if c == 2:
		print('atari:a-b-d-c')
		break

	if e == 0:
		h = random.randint(1,2)
		print('e')
	elif e == 1:
		f = random.randint(1,2)
		print('e')
	elif e == 2:
		print('atari:a-e')
		break
	
	if f == 1:
		g =2
		print('f')
	elif f == 2:
		print('atari:a-e-f')
		break

	if g == 2:
		print('atari:a-e-f-g')
		break

	if h == 1:
		i = 2
		print('h')
	elif h == 2:
		print('atari:a-e-h')
		break

	if i == 2:
		print('atari:a-e-h-i')
		break
