#要素を液体、1次元リスト部分を固体(溶けない)、2次元リスト部分をコップに見立てて
#ドリンクバーで遊ぶためのシミュレーター

#量を問う
solnum = int(input('固体量:'))
liqnum = int(input('液体量:'))

cup = []

#量に応じて固体から投入していく
for i in range(1,solnum+1):
	ip1 = input('固体名:')
	ice = [ip1]
	cup.append(ice)

for j in range(1,liqnum+1):
	ip2 = input('液体名:')
	water = [ip2]
	cup.extend(water)#(cup+=waterでも可)

print('完成品:',cup)#出来上がった飲み物
